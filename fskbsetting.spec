Name:		fskbsetting
Version:	0.3.2
Release:	4
License:	GPLv3
Summary:	GUI Front-end for setxkbmap Command
URL:		http://code.google.com/p/mandriva-lxde
Group:		System/X11
Source0:	http://mandriva-lxde.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		fskbsetting-0.3.2-wxgtku.patch
Patch1:		fskbsetting-0.3.2-automake-1.13-build-fix.patch
BuildRequires:	gcc-c++
BuildRequires:	intltool
BuildRequires:	automake
BuildRequires:	wxgtku-devel

%description
fsKBSetting is GUI front-end for setxkbmap command.

%prep
%setup -q
%patch0 -p1 -b .wxgtku~
%patch1 -p1 -b .am113~
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

%changelog
* Thu Jan 19 2012 Andrey Bondrov <abondrov@mandriva.org> 0.3.2-3mdv2012.0
+ Revision: 762258
- Switch to utf8 version of wxGTK2.8, add patch 0 for that

* Thu Aug 11 2011 Александр Казанцев <kazancas@mandriva.org> 0.3.2-2
+ Revision: 693938
+ rebuild (emptylog)

* Thu Aug 11 2011 Александр Казанцев <kazancas@mandriva.org> 0.3.2-1
+ Revision: 693930
- 0.3.2 Add localization support for language and layout

* Tue Aug 09 2011 Александр Казанцев <kazancas@mandriva.org> 0.3.1-1
+ Revision: 693751
- update to 0.3.1. drop patches and fix bug with fogotten layouts without X-restart. fix url

* Wed Aug 03 2011 Александр Казанцев <kazancas@mandriva.org> 0.3-4
+ Revision: 692996
- fix .desktop file

* Tue Dec 28 2010 Александр Казанцев <kazancas@mandriva.org> 0.3-3mdv2011.0
+ Revision: 625675
-initial release
- import fskbsetting


* Thu Sep 7 2010 Alexander Kazancev <kazancas@mandriva.ru> 0.3-3
- fix multiple add to desktop file

* Mon Aug 9 2010 Alexander Kazancev <kazancas@mandriva.ru>
- Add patch for create .config/autostart file

* Mon Jul 12 2010 lazy.kent.suse@gmail.com
- initial package created - 0.3
- corrected desktop-file
- added icon
