Summary:	eAudio, formerly known as eMusic
Summary(pl):	eAudio, znane kiedy¶ jako eMusic
Name:		eAudio
Version:	0.9.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://linux.tucows.com/files/gnome/media/%{name}-DR%{version}.tar.gz
Patch0:		%{name}-opt.patch
# 404, but no working URL
URL:		http://www.icom.net/~smelecat/emp3/
BuildRequires:	gtk+-devel >= 1.1.15
BuildRequires:	imlib-devel >= 1.9.2
BuildRequires:	esound >= 0.2.7
BuildRequires:	libungif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	eMusic

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
It's an "enlightened" sound file player gui type thing. Enlightened
meaning it's highly configurable, graphics wise.

%description -l pl
W pakiecie znajduje siê "o¶wiecony" odtwarzacz d¼wiêków dla
Enlightenmenta. O¶wiecony to znaczy bardzo ³atwo daj±cy siê
konfigurowaæ - w sposób graficzny.

%prep
%setup -q -n %{name}-DR%{version}
%patch -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/eAudio
%{_datadir}/eAudio
