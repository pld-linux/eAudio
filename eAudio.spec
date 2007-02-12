Summary:	eAudio, formerly known as eMusic
Summary(pl.UTF-8):	eAudio, znane kiedyś jako eMusic
Name:		eAudio
Version:	0.9.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
#Source0:	http://linux.tucows.com/files/gnome/media/%{name}-DR%{version}.tar.gz
Source0:	%{name}-DR%{version}.tar.gz
# Source0-md5:	563caabcbf4e8a4db47889ee9af3b98b
Patch0:		%{name}-opt.patch
#URL:		http://www.icom.net/~smelecat/emp3/
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

%description -l pl.UTF-8
W pakiecie znajduje się "oświecony" odtwarzacz dźwięków dla
Enlightenmenta. Oświecony to znaczy bardzo łatwo dający się
konfigurować - w sposób graficzny.

%prep
%setup -q -n %{name}-DR%{version}
%patch0 -p1

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/eAudio
%{_datadir}/eAudio
