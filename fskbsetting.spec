Name:		fskbsetting
Version:	0.3.2
Release:	%mkrel 3
License:	GPLv3
Summary:	GUI Front-end for setxkbmap Command
URL:		http://code.google.com/p/mandriva-lxde
Group:		System/X11
Source0:	http://mandriva-lxde.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		fskbsetting-0.3.2-wxgtku.patch
BuildRequires:	gcc-c++
BuildRequires:	intltool
BuildRequires:	automake
BuildRequires:	wxgtku-devel

%description
fsKBSetting is GUI front-end for setxkbmap command.

%prep
%setup -q
%patch0 -p1 -b .wxgtku~

%build
autoreconf --force --install --symlink
%configure2_5x
%make

%install
%__rm -rf %{buildroot}

%makeinstall_std
%__mkdir_p %{buildroot}%{_datadir}/pixmaps
%__rm -rf %{buildroot}%{_prefix}/doc/%{name}

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TRANSLATORS
%{_datadir}/%{name}
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
