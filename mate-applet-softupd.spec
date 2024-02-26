Summary:	Software Updates applet for MATE desktop
Name:		mate-applet-softupd
Version:	0.4.8
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		https://github.com/assen-totin/mate-applet-softupd
Source:		https://github.com/assen-totin/mate-applet-softupd/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		mate-applet-softupdhimBHs0.4.8-add-dnfdrake.patch

BuildRequires:	gettext-devel
BuildRequires:	mate-panel-devel
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	dnf
BuildRequires:	dnfdrake

Requires:	dnf
Requires:	dnfdrake

%description
This is a MATE panel applet to notify when software updates
become available.

The notification is displayed in two ways: 
 *  by changing the icon of the applet
 *  by sending a notification to the notification-daemon

The information is obtained from dnf.

%files -f %{name}.lang
%license COPYING
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%{_libexecdir}/softupd_applet
%dir %{_datadir}/mate-panel/
%dir %{_datadir}/mate-panel/applets/
%{_datadir}/mate-panel/applets/org.mate.applets.SoftupdApplet.mate-panel-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.SoftupdApplet.service
%{_datadir}/pixmaps/applet_softupd*.png
%{_iconsdir}/hicolor/*/apps/applet_softupd.png

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
NO_CONFIGURE=1 sh ./autogen.sh
%configure \
	--enable-gtk=3		 \
	--enable-backend=dnf \
	--enable-installer=dnfdrake.gambas
%make_build

%install
%make_install

# install docs manually
rm -fr %{buildroot}%{_docdir}/%{name}

# locales
%find_lang %{name} --with-gnome --all-name

