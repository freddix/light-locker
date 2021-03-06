Summary:	Scrren locking application for use with LightDM
Name:		light-locker
Version:	1.6.0
Release:	1
License:	GPL v2/LGPL
Group:		X11/Applications
Source0:	https://github.com/the-cavalry/light-locker/releases/download/v%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	7f2425887d7bc8e86b53846f400d4ace
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk+-devel
BuildRequires:	pkg-config
BuildRequires:	systemd-devel
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXxf86misc-devel
Requires(post,postun):	glib-gio-gsettings
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
light-locker is a simple locker (forked from gnome-screensaver) that
aims to have simple, sane, secure defaults and be well integrated with
the desktop while not carrying any desktop-specific dependencies.

%prep
%setup -q

%build
%configure \
	--disable-schemas-compile   \
	--disable-silent-rules	    \
	--with-console-kit=no	    \
	--with-gtk2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/light-locker
%attr(755,root,root) %{_bindir}/light-locker-command
%{_datadir}/glib-2.0/schemas/apps.light-locker.gschema.xml
%{_sysconfdir}/xdg/autostart/light-locker.desktop
%{_mandir}/man1/light-locker*1*

