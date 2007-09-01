Name:		qstardict
Version:	0.06
Release:	%mkrel 1
License:	GPL
URL:		http://qstardict.ylsoftware.com
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildRequires:	qt4-devel glib2-devel desktop-file-utils ImageMagick
Source:		%{name}-%{version}.tar.bz2
Group:		Office
Summary:	StarDict clone written in Qt4
Requires:	stardict-dictionary = 2.4.2

%description
StarDict is a clone of StarDict written in Qt4.
Main features:
* Full support of StarDict dictionaries
* Working in system tray
* Scanning mouse selection and showing popup window with translation of selected word

%prep
%setup -q

%build
%{qt4dir}/bin/qmake
%make

%install
install -D -m755 bin/qstardict %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_iconsdir}
convert -resize 32x32 resources/qstardict.png %{buildroot}%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}%{_liconsdir}
convert -resize 48x48 resources/qstardict.png %{buildroot}%{_liconsdir}/%{name}.png
mkdir -p %{buildroot}%{_miconsdir}
convert -resize 16x16 resources/qstardict.png %{buildroot}%{_miconsdir}/%{name}.png

mkdir -p %buildroot%{_datadir}/applications
desktop-file-install --vendor='' \
	--dir=%buildroot%{_datadir}/applications \
	--remove-category='Utility' \
	--add-category='Office' \
	resources/qstardict.desktop

%clean
rm -rf %{buildroot}

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
