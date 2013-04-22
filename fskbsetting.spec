Summary:	GUI Front-end for setxkbmap Command
Name:		fskbsetting
Version:	0.3.2
Release:	4
License:	GPLv3
Group:		System/X11
Url:		http://code.google.com/p/mandriva-lxde
Source0:	http://mandriva-lxde.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		fskbsetting-0.3.2-wxgtku.patch
Patch1:		fskbsetting-0.3.2-automake-1.13-build-fix.patch

BuildRequires:	gcc-c++
BuildRequires:	intltool
BuildRequires:	wxgtku-devel

%description
fsKBSetting is GUI front-end for setxkbmap command.

%prep
%setup -q
%apply_patches
autoreconf --force --install --symlink

%build
%configure2_5x
%make

%install
%makeinstall_std
mkdir -p %{buildroot}%{_datadir}/pixmaps
rm -r %{buildroot}%{_prefix}/doc/%{name}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README TRANSLATORS
%{_datadir}/%{name}
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop

