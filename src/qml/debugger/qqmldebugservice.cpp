/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtQml module of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL21$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see http://www.qt.io/terms-conditions. For further
** information use the contact form at http://www.qt.io/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 2.1 or version 3 as published by the Free
** Software Foundation and appearing in the file LICENSE.LGPLv21 and
** LICENSE.LGPLv3 included in the packaging of this file. Please review the
** following information to ensure the GNU Lesser General Public License
** requirements will be met: https://www.gnu.org/licenses/lgpl.html and
** http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
**
** As a special exception, The Qt Company gives you certain additional
** rights. These rights are described in The Qt Company LGPL Exception
** version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
**
** $QT_END_LICENSE$
**
****************************************************************************/

#include "qqmldebugservice_p.h"
#include "qqmldebugservice_p_p.h"
#include "qqmldebugserver_p.h"
#include <private/qqmldata_p.h>
#include <private/qqmlcontext_p.h>

#include <QtCore/QDebug>
#include <QtCore/QStringList>
#include <QtCore/QFileInfo>

QT_BEGIN_NAMESPACE

QQmlDebugServicePrivate::QQmlDebugServicePrivate(const QString &name, float version) :
    name(name), version(version), state(QQmlDebugService::NotConnected)
{
}

QQmlDebugService::QQmlDebugService(const QString &name, float version, QObject *parent)
    : QObject(*(new QQmlDebugServicePrivate(name, version)), parent)
{
    QQmlDebugServer::instance(); // create it when it isn't there yet.
}

QQmlDebugService::QQmlDebugService(QQmlDebugServicePrivate &dd, QObject *parent)
    : QObject(dd, parent)
{
}

/**
  Registers the service. This should be called in the constructor of the inherited class. From
  then on the service might get asynchronous calls to messageReceived().
  */
QQmlDebugService::State QQmlDebugService::registerService()
{
    Q_D(QQmlDebugService);
    QQmlDebugServer *server = QQmlDebugServer::instance();

    if (!server)
        return NotConnected;

    if (server->serviceNames().contains(d->name)) {
        qWarning() << "QQmlDebugService: Conflicting plugin name" << d->name;
    } else {
        server->addService(this);
    }
    return state();
}

QQmlDebugService::~QQmlDebugService()
{
    if (QQmlDebugServer *inst = QQmlDebugServer::instance())
        inst->removeService(this);
}

const QString &QQmlDebugService::name() const
{
    Q_D(const QQmlDebugService);
    return d->name;
}

float QQmlDebugService::version() const
{
    Q_D(const QQmlDebugService);
    return d->version;
}

QQmlDebugService::State QQmlDebugService::state() const
{
    Q_D(const QQmlDebugService);
    return d->state;
}

namespace {
class ObjectReferenceHash : public QObject
{
    Q_OBJECT
public:
    ObjectReferenceHash() : nextId(0) {}

    QHash<QObject *, int> objects;
    QHash<int, QObject *> ids;

    int nextId;

private slots:
    void remove(QObject *obj);
};
}
Q_GLOBAL_STATIC(ObjectReferenceHash, objectReferenceHash)

void ObjectReferenceHash::remove(QObject *obj)
{
    QHash<QObject *, int>::Iterator iter = objects.find(obj);
    if (iter != objects.end()) {
        ids.remove(iter.value());
        objects.erase(iter);
    }
}

/*!
    Returns a unique id for \a object.  Calling this method multiple times
    for the same object will return the same id.
*/
int QQmlDebugService::idForObject(QObject *object)
{
    if (!object)
        return -1;

    ObjectReferenceHash *hash = objectReferenceHash();
    QHash<QObject *, int>::Iterator iter = hash->objects.find(object);

    if (iter == hash->objects.end()) {
        int id = hash->nextId++;
        hash->ids.insert(id, object);
        iter = hash->objects.insert(object, id);
        connect(object, SIGNAL(destroyed(QObject*)), hash, SLOT(remove(QObject*)));
    }
    return iter.value();
}

/*!
    Returns the mapping of objects to unique \a ids, created through calls to idForObject().
*/
const QHash<int, QObject *> &QQmlDebugService::objectsForIds()
{
    return objectReferenceHash()->ids;
}

bool QQmlDebugService::isDebuggingEnabled()
{
    return QQmlDebugServer::instance() != 0;
}

bool QQmlDebugService::hasDebuggingClient()
{
    return QQmlDebugServer::instance() != 0
            && QQmlDebugServer::instance()->hasDebuggingClient();
}

bool QQmlDebugService::blockingMode()
{
    return QQmlDebugServer::instance() != 0
            && QQmlDebugServer::instance()->blockingMode();
}

QString QQmlDebugService::objectToString(QObject *obj)
{
    if(!obj)
        return QStringLiteral("NULL");

    QString objectName = obj->objectName();
    if(objectName.isEmpty())
        objectName = QStringLiteral("<unnamed>");

    QString rv = QString::fromUtf8(obj->metaObject()->className()) +
            QLatin1String(": ") + objectName;

    return rv;
}

void QQmlDebugService::sendMessage(const QByteArray &message)
{
    sendMessages(QList<QByteArray>() << message);
}

void QQmlDebugService::sendMessages(const QList<QByteArray> &messages)
{
    if (state() != Enabled)
        return;

    if (QQmlDebugServer *inst = QQmlDebugServer::instance())
        inst->sendMessages(this, messages);
}

void QQmlDebugService::stateAboutToBeChanged(State)
{
}

void QQmlDebugService::stateChanged(State)
{
}

void QQmlDebugService::messageReceived(const QByteArray &)
{
}

void QQmlDebugService::engineAboutToBeAdded(QQmlEngine *engine)
{
    emit attachedToEngine(engine);
}

void QQmlDebugService::engineAboutToBeRemoved(QQmlEngine *engine)
{
    emit detachedFromEngine(engine);
}

void QQmlDebugService::engineAdded(QQmlEngine *)
{
}

void QQmlDebugService::engineRemoved(QQmlEngine *)
{
}

QQmlDebugStream::QQmlDebugStream()
    : QDataStream()
{
    setVersion(QQmlDebugServer::s_dataStreamVersion);
}

QQmlDebugStream::QQmlDebugStream(QIODevice *d)
    : QDataStream(d)
{
    setVersion(QQmlDebugServer::s_dataStreamVersion);
}

QQmlDebugStream::QQmlDebugStream(QByteArray *ba, QIODevice::OpenMode flags)
    : QDataStream(ba, flags)
{
    setVersion(QQmlDebugServer::s_dataStreamVersion);
}

QQmlDebugStream::QQmlDebugStream(const QByteArray &ba)
    : QDataStream(ba)
{
    setVersion(QQmlDebugServer::s_dataStreamVersion);
}

QT_END_NAMESPACE

#include "qqmldebugservice.moc"
