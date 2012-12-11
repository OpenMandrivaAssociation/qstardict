Name:		qstardict
Version:	1.0.1
Release:	%mkrel 4
# fwang: this one is GPLv2 only, because in the version upgrade of
# 0.06 -> 0.07, it changed from GPLv3 to GPLv2.
License:	GPLv2
URL:		http://qstardict.ylsoftware.com
BuildRequires:	qt4-devel glib2-devel desktop-file-utils imagemagick
BuildRequires:	kdelibs4-devel
Source0:	http://qstardict.ylsoftware.com/files/%{name}-%{version}.tar.bz2
Patch0:		qstardict-1.0.1-mdv-glib.patch
Group:		Office
Summary:	StarDict clone written in Qt4
Requires:	stardict-dictionary = 2.4.2

%description
QStarDict is a dictionary program written using Qt4. The user interface is
similar to StarDict. The latest version is 1.0.1.

Main features

* Full support of StarDict 2.x dictionaries
* Working in system tray
* Scanning mouse selection and showing popup window with translation
  of selected word
* Translations reformatting
* Plugins support

%package -n plasma-applet-%{name}
Group:		Graphical desktop/KDE
Summary:	Plasma applet of qstardict
Requires:	%name = %version

%description -n plasma-applet-%{name}
This package contains kde plasma applet of qstardict.

%prep
%setup -q
%patch0 -p1

%build
%qmake_qt4 PLUGINS_DIR=%_libdir/%name/plugins ENABLED_PLUGINS="stardict web"
%make

cd kdeplasma
%cmake_kde4
%make

%install
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


%changelog
* Wed Feb 01 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.0.1-4mdv2011.0
+ Revision: 770352
- update to 1.0.1

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.13.1-4mdv2011.0
+ Revision: 614679
- the mass rebuild of 2010.1 packages

* Fri Apr 30 2010 Funda Wang <fwang@mandriva.org> 0.13.1-3mdv2010.1
+ Revision: 541301
- fix build with gcc 4.4

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Mar 11 2009 Funda Wang <fwang@mandriva.org> 0.13.1-2mdv2009.1
+ Revision: 353779
- add kde4 plasma applet

* Tue Feb 10 2009 Funda Wang <fwang@mandriva.org> 0.13.1-1mdv2009.1
+ Revision: 339177
- fix file list
- New version 0.13.1

* Tue Feb 03 2009 Funda Wang <fwang@mandriva.org> 0.13-1mdv2009.1
+ Revision: 337023
- enable plugins
- New verison 0.13

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Tue Aug 05 2008 Funda Wang <fwang@mandriva.org> 0.12.9-2mdv2009.0
+ Revision: 263693
- rebuild against new compile flags

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jun 11 2008 Funda Wang <fwang@mandriva.org> 0.12.9-1mdv2009.0
+ Revision: 218145
- New version 0.12.9

* Wed Jun 11 2008 Funda Wang <fwang@mandriva.org> 0.12.8-1mdv2009.0
+ Revision: 218085
- New version 0.12.8

* Wed Apr 16 2008 Funda Wang <fwang@mandriva.org> 0.12.7-2mdv2009.0
+ Revision: 194547
- move plugin dir
- New version 0.12.7

  + Thierry Vignaud <tv@mandriva.org>
    - fix description-line-too-long
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Nov 12 2007 Funda Wang <fwang@mandriva.org> 0.08-1mdv2008.1
+ Revision: 108061
- New version 0.08

* Fri Sep 07 2007 Funda Wang <fwang@mandriva.org> 0.07-1mdv2008.0
+ Revision: 82013
- New version 0.07

* Sat Sep 01 2007 Funda Wang <fwang@mandriva.org> 0.06-1mdv2008.0
+ Revision: 77348
- New version 0.06

* Wed Aug 29 2007 Funda Wang <fwang@mandriva.org> 0.05-1mdv2008.0
+ Revision: 73345
- convert suse style to mandriva style
- Import qstardict



* Tue Jul 31 2007 - Petr Vanek <petr@scribus.info>
- updated to 0.05
* Fri Jul 27 2007 - Nikolay Derkach <nderkach@gmail.com>
- update to 0.04
* Sun Jul 08 2007 - Nikolay Derkach <nderkach@gmail.com>
- initial package
