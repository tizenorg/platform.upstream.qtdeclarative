# The MIT License (MIT)
# 
# Copyright (c) 2013 Tomasz Olszak <olszak.tomasz@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# This file is based on qtdeclarative.spec from Mer project
# http://merproject.org

Name:       qt5-qtdeclarative
Summary:    Qt Declarative library
Version:    5.2.96+rc2
Release:    0%{?dist}
Group:      Base/Libraries
License:    LGPL-2.1+ or GPL-3.0
URL:        http://qt.digia.com
Source0:    %{name}-%{version}.tar.bz2
Source1001: %{name}.manifest
Source1010: %{name}-examples.sh
Source1011: %{name}-examples.desktop
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtopengl-devel
BuildRequires:  qt5-qtsql-devel
BuildRequires:  qt5-qttest-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  qt5-qmake
BuildRequires:  fdupes
BuildRequires:  python
BuildRequires:  gdb

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Declarative library


%package devel
Summary:    Qt Declarative - development files
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   qt5-qtsql-devel
Requires:   qt5-qtnetwork-devel

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Declarative library development files

%package qtquicktest
Summary:    Qt Declarative QtQuickTest library
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtquicktest
This package contains the QtQuickTest library for QtDeclarative module

%package qtquicktest-devel
Summary:    Qt Declarative QtQuickTest - development files
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-devel = %{version}-%{release}
Requires:   qt5-qtdeclarative-qtquicktest = %{version}-%{release}

%description qtquicktest-devel
This package contains the development headers for QtQuickTest library

%package qtquick
Summary:    Qt Declarative - QtQuick library
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description qtquick
This package contains the QtQuick QML support library

%package qtquick-devel
Summary:    Qt Declarative - QtQuick development files
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   qt5-qtdeclarative-qtquick = %{version}-%{release}

%description qtquick-devel
This package contains the development headers for legacy QtQuick 1
QML support library

%package qtquick-widgets
Summary:    Qt Declarative - QtQuick Widgets library
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description qtquick-widgets
This package contains the QtQuickWidgets QML support library

%package qtquick-widgets-devel
Summary:    Qt Declarative - QtQuick Widgets development files
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   qt5-qtdeclarative-qtquick-widgets = %{version}-%{release}

%description qtquick-widgets-devel
This package contains the development headers for QtQuickWidgets 
library 

%package qtquickparticles
Summary:    Qt Declarative - QtQuick Particles library
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description qtquickparticles
This package contains the QtQuick Particles support library

%package qtquickparticles-devel
Summary:    Qt Declarative - QtQuick Particles development files
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   qt5-qtdeclarative-qtquickparticles = %{version}-%{release}

%description qtquickparticles-devel
This package contains the development headers for QtQuickParticles
QML support library


%package qtdeclarativetools-devel
Summary:    Qt Declarative QtQmlDevTools - development files
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-devel = %{version}-%{release}
Requires:   qt5-qtdeclarative-devel = %{version}-%{release}

%description qtdeclarativetools-devel
This package contains the development headers for QtQmlDevTools



#### Small plugin and import packages

%package import-folderlistmodel
Summary:    Qt Declarative folderlistmodel plugin
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description import-folderlistmodel
This package provides the QtQml folderlistmodel plugin

%package import-settings
Summary:    Qt Declarative settings plugin
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description import-settings
This package provides the QtQml settings plugin

%package import-localstorageplugin
Summary:    Qt LocalStorage plugin
Requires:   %{name} = %{version}-%{release}

%description import-localstorageplugin
This package provided the Qt LocalStorage plugin

%package plugin-qmlinspector
Summary:    Qt Declarative QML inspector plugin
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description plugin-qmlinspector
This package provides the QML inspector plugin

%package plugin-accessible
Summary:    Qt Declarative accessible plugin
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description plugin-accessible
This package provides the QML accessible plugin


%package import-qtquick2plugin
Summary:    Qt Declarative QtQuick 2 support plugin
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description import-qtquick2plugin
This package provides the QtQuick 2 support plugin

%package import-qttest
Summary:    Qt Declarative QtTest plugin
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description import-qttest
This package provides the QtQml QtTest plugin

%package import-particles2
Summary:    Qt Declarative Particles plugin
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description import-particles2
This package provides the QtQml Particles.2 plugin

%package import-window2
Summary:    Qt Declarative Window plugin
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description import-window2
This package provides the QtQml Window.2 plugin

%package import-models2
Summary:    Qt Declarative models plugin
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description import-models2
This package provides the QtDeclarative models plugin for QtQuick 2.0

%package import-xmllistmodel
Summary:    Qt Declarative XmlListModel plugin
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description import-xmllistmodel
This package provides the QtDeclarative XmlListModel plugin for QtQuick 2.0

%package qmlscene
Summary:    QML scene viewer
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description qmlscene
This package contains the QML viewer for QtQuick 2.0 files.

%package qml
Summary:    QML viewer
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description qml
This package contains recommended the QML viewer for QtQuick 2.0 files. It supersedes the qmlscene.

%package devel-tools
Summary:    QML development tools
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel-tools
This package contains QML debugging and development tools


%package examples
Summary:    QML and Qt Quick Examples
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   qt5-plugin-imageformat-jpeg
Requires:   qt5-qtdeclarative-import-folderlistmodel
Requires:   qt5-qtdeclarative-import-models2
Requires:   qt5-qtdeclarative-import-multimedia
Requires:   qt5-qtdeclarative-import-particles2
Requires:   qt5-qtdeclarative-import-qtquick2plugin
Requires:   qt5-qtdeclarative-import-window2
Requires:   qt5-qtdeclarative-import-xmllistmodel
Requires:   qt5-qtdeclarative-qmlscene

%description examples
This package contains QML and Qt Quick Examples for developers.
Those can run used with luncher script or using interperter :
ie: qml ./examples/quick/demos/*/*.qml



#### Build section

%prep
%setup -q -n %{name}-%{version}/qtdeclarative
cp %{SOURCE1001} .

%build
export QTDIR=/usr/share/qt5
touch .git

qmake -qt=5
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install
# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;
# Remove unneeded .la files
rm -f %{buildroot}%{_libdir}/*.la

# We don't need qt5/Qt/
rm -rf %{buildroot}%{_includedir}/qt5/Qt

# Manually copy qmldevtools static library
cp lib/libQt5QmlDevTools.a %{buildroot}%{_libdir}
%fdupes %{buildroot}%{_libdir}
%fdupes %{buildroot}%{_includedir}

# Manually copy examples
install -d "%{buildroot}%{_datadir}/qt5/%{name}/"
cp -rf examples "%{buildroot}%{_datadir}/qt5/%{name}/"
install -d "%{buildroot}%{_bindir}/"
install %{SOURCE1010} "%{buildroot}%{_bindir}/"
install -d "%{buildroot}%{_datadir}/applications/"
install %{SOURCE1011} "%{buildroot}%{_datadir}/applications/"
install -d "%{buildroot}%{_datadir}/icons/default/small/"
install ./src/quick/doc/images/declarative-qtlogo.png "%{buildroot}%{_datadir}/icons/default/small/%{name}.png"

#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig

%post qtquicktest
/sbin/ldconfig
%postun qtquicktest
/sbin/ldconfig

%post qtquick
/sbin/ldconfig
%postun qtquick
/sbin/ldconfig


%post qtquickparticles
/sbin/ldconfig
%postun qtquickparticles
/sbin/ldconfig


#### File section


%files
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/libQt5Qml.so.5
%{_libdir}/libQt5Qml.so.5.*

# FIXME: the provided .pc file is empty!
# Find out what gives and find a clean resolution
%files devel
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/libQt5Qml.so
%{_libdir}/libQt5Qml.prl
%{_libdir}/pkgconfig/Qt5Qml.pc
%{_includedir}/qt5/QtQml
%{_datadir}/qt5/mkspecs/modules/qt_lib_qml.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_qml_private.pri
%{_libdir}/cmake


%files qtquick
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/libQt5Quick.so.5
%{_libdir}/libQt5Quick.so.5.*

%files qtquick-devel
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/libQt5Quick.so
%{_libdir}/libQt5Quick.prl
%{_libdir}/pkgconfig/Qt5Quick.pc
%{_includedir}/qt5/QtQuick
%{_datadir}/qt5/mkspecs/modules/qt_lib_quick.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_quick_private.pri

%files qtquick-widgets
%{_libdir}/libQt5QuickWidgets.so.5
%{_libdir}/libQt5QuickWidgets.so.5.*

%files qtquick-widgets-devel
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/libQt5QuickWidgets.so
%{_libdir}/libQt5QuickWidgets.prl
%{_libdir}/pkgconfig/Qt5QuickWidgets.pc
%{_includedir}/qt5/QtQuickWidgets
%{_datadir}/qt5/mkspecs/modules/qt_lib_quickwidgets.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_quickwidgets_private.pri

%files qmlscene
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_qt5_bindir}/qmlscene

%files qml
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_qt5_bindir}/qml

%files devel-tools
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_qt5_bindir}/qmlplugindump
%{_qt5_bindir}/qmlprofiler
%{_qt5_bindir}/qmltestrunner
%{_qt5_bindir}/qmlmin
%{_qt5_bindir}/qmlbundle
%{_qt5_bindir}/qmlimportscanner
%{_qt5_bindir}/qmljs

%files import-folderlistmodel
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/qml/Qt/labs/folderlistmodel/*

%files import-localstorageplugin
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/qml/QtQuick/LocalStorage

%files plugin-qmlinspector
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/plugins/qmltooling/*

%files plugin-accessible
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/plugins/accessible/libqtaccessiblequick.so

%files import-qttest
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/qml/QtTest

%files import-qtquick2plugin
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/qml/QtQuick.2

%files import-particles2
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/qml/QtQuick/Particles.2

%files import-window2
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/qml/QtQuick/Window.2

%files import-models2
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/qml/QtQml/Models.2

%files import-xmllistmodel
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/qml/QtQuick/XmlListModel



%files qtquicktest
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/libQt5QuickTest.so.5
%{_libdir}/libQt5QuickTest.so.5.*

%files qtquicktest-devel
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_includedir}/qt5/QtQuickTest
%{_libdir}/libQt5QuickTest.so
%{_libdir}/libQt5QuickTest.prl
%{_libdir}/pkgconfig/Qt5QuickTest.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_qmltest.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_qmltest_private.pri

%files qtquickparticles
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/libQt5QuickParticles.so.5
%{_libdir}/libQt5QuickParticles.so.5.*

%files qtquickparticles-devel
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_includedir}/qt5/QtQuickParticles
%{_libdir}/libQt5QuickParticles.so
%{_libdir}/libQt5QuickParticles.prl
%{_libdir}/pkgconfig/Qt5QuickParticles.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_quickparticles_private.pri

%files qtdeclarativetools-devel
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/libQt5QmlDevTools.a
%{_libdir}/libQt5QmlDevTools.prl
%{_libdir}/pkgconfig/Qt5QmlDevTools.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_qmldevtools_private.pri


%files import-settings
%{_libdir}/qt5/qml/Qt/labs/settings

%files examples
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_bindir}/%{name}-examples.sh
%{_datadir}/applications/%{name}-examples.desktop
%{_datadir}/icons/default/small/%{name}.png
%{_datadir}/qt5/%{name}/examples/*


#### No changelog section, separate $pkg.changelog contains the history
