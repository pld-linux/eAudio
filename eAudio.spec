Summary:	eAudio, formerly known as eMusic
Summary(pl):	eAudio, znane kiedy� jako eMusic
Name:		eAudio
Version:	0.9.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://linux.tucows.com/files/gnome/media/%{name}-DR%{version}.tar.gz
# Source0-md5:	763f4e11f5f0e939f8d5437e1c9cfa88
Patch0:		%{name}-opt.patch
# 404, but no working URL
URL:		http://www.icom.net/~smelecat/emp3/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound >= 0.2.7
BuildRequires:	gtk+-devel >= 1.1.15
BuildRequires:	imlib-devel >= 1.9.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	eMusic


%description
It's an "enlightened" sound file player gui type thing. Enlightened
meaning it's highly configurable, graphics wise.

%description -l pl
W pakiecie znajduje si� "o�wiecony" odtwarzacz d�wi�k�w dla
Enlightenmenta. O�wiecony to znaczy bardzo �atwo daj�cy si�
konfigurowa� - w spos�b graficzny.

%prep
%setup -q -n %{name}-DR%{version}
%patch -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/eAudio
%{_datadir}/eAudio
