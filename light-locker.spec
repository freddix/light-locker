Summary:	Scrren locking application for use with LightDM
Name:		light-locker
Version:	0.1.0
Release:	2
License:	GPL v2/LGPL
Group:		X11/Applications
Source0:	http://rhaalovely.net/stuff/%{name}-%{version}.tar.bz2
# Source0-md5:	52984b8c7066b63e1c5398859e36a255
BuildRequires:	gtk+-devel
BuildRequires:	pkg-config
BuildRequires:	systemd-devel
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXxf86misc-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
light-locker is a simple locker (forked from gnome-screensaver) that
aims to have simple, sane, secure defaults and be well integrated with
the desktop while not carrying any desktop-specific dependencies.

%prep
%setup -q

%build
%configure \
	--with-gtk2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/light-locker
%attr(755,root,root) %{_bindir}/light-locker-command
%{_desktopdir}/light-locker.desktop
%{_mandir}/man1/light-locker*1*

