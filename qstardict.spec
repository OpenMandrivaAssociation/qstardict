Name:		qstardict
Version:	0.13.1
Release:	%mkrel 2
# fwang: this one is GPLv2 only, because in the version upgrade of
# 0.06 -> 0.07, it changed from GPLv3 to GPLv2.
License:	GPLv2
URL:		http://qstardict.ylsoftware.com
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildRequires:	qt4-devel glib2-devel desktop-file-utils imagemagick
BuildRequires:	kdelibs4-devel
Source:		%{name}-%{version}.tar.bz2
Group:		Office
Summary:	StarDict clone written in Qt4
Requires:	stardict-dictionary = 2.4.2

%description
StarDict is a clone of StarDict written in Qt4.
Main features:
* Full support of StarDict dictionaries
* Working in system tray
* Scanning mouse selection and showing popup window with translation of
  selected word

%package -n plasma-applet-%{name}
Group:		Graphical desktop/KDE
Summary:	Plasma applet of qstardict
Requires:	%name = %version

%description -n plasma-applet-%{name}
This package contains kde plasma applet of qstardict.

%prep
%setup -q

%build
%qmake_qt4 PLUGINS_DIR=%_libdir/%name/plugins ENABLED_PLUGINS="stardict web"
%make

cd kdeplasma
%cmake_kde4
%make

%install
rm -fr %buildroot
make install INSTALL_ROOT=%{buildroot}

pushd kdeplasma/build
%makeinstall_std
popd

mkdir -p %{buildroot}%{_iconsdir}
convert -resize 32x32 qstardict/qstardict.png %{buildroot}%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}%{_liconsdir}
convert -resize 48x48 qstardict/qstardict.png %{buildroot}%{_liconsdir}/%{name}.png
mkdir -p %{buildroot}%{_miconsdir}
convert -resize 16x16 qstardict/qstardict.png %{buildroot}%{_miconsdir}/%{name}.png

mkdir -p %buildroot%{_datadir}/applications
desktop-file-install --vendor='' \
	--dir=%buildroot%{_datadir}/applications \
	--remove-category='Utility' \
	--add-category='Office' \
	--remove-key='Encoding' \
	qstardict/qstardict.desktop

rm -fr %buildroot%_datadir/doc

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog THANKS
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

%files -n plasma-applet-%{name}
%defattr(-,root,root)
%_kde_libdir/kde4/*.so
%_kde_services/*.desktop
