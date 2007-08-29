#
# spec file for package QStarDict
#
# Copyright (c) 2007 Nikolay Derkach
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

Name:           qstardict
Version:        0.05
Release:        2.1
License:        GPL
URL:            http://qstardict.ylsoftware.com
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libqt4-devel >= 4.2.0 update-desktop-files glib2-devel
Source:       %{name}-%{version}.tar.bz2
Group:        Productivity/Office/Dictionary
Summary:      StarDict clone written in Qt4.

%description
StarDict is a clone of StarDict written in Qt4.
Main features:
* Full support of StarDict dictionaries
* Working in system tray
* Scanning mouse selection and showing popup window with translation of selected word

Authors:
--------
    Alexander Rodin <rodin.alexander@gmail.com>

%prep
%setup -n %{name}-%{version} -q

%build
qmake
make %{?jobs:-j %jobs}

%install
%__install -d -m 755 %{buildroot}%{_bindir}
%__install -p -m 755 bin/qstardict %{buildroot}%{_bindir}

%__install -d -m 755 %{buildroot}%{_datadir}/pixmaps/
%__install -p -m 644 resources/qstardict.png %{buildroot}%{_datadir}/pixmaps/

%suse_update_desktop_file -c %{name} "QStarDict" "QStarDict Dictionary" %{name} "%{name}.png" Office Dictionary

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/qstardict
%{_datadir}/applications/qstardict.desktop
%{_datadir}/pixmaps/qstardict.png
