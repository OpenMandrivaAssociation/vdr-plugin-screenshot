
%define plugin	screenshot
%define name	vdr-plugin-%plugin
%define version	0.0.13
%define rel	2

Summary:	VDR plugin: Takes screenshots
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.joachim-wilke.de/vdr-screenshot.htm
Source:		vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
With this plugin you can take still images of your screen. After installing
the plugin, a new mainmenu entry "Screenshot" will show up. Each time you
select this item, a file /tmp/title-yyyymmdd-hhmmss.jpg will be created,
where title is the current transmission or the recording currently replayed.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.13-2mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Wed Jul 15 2009 Anssi Hannula <anssi@mandriva.org> 0.0.13-1mdv2010.0
+ Revision: 396111
- new version
- drop vdr 1.6 i18n patch, fixed upstream

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.11-15mdv2009.1
+ Revision: 359362
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.11-14mdv2009.0
+ Revision: 197974
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.11-13mdv2009.0
+ Revision: 197719
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.11-12mdv2008.1
+ Revision: 145198
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.11-11mdv2008.1
+ Revision: 103205
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.11-10mdv2008.0
+ Revision: 50042
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.11-9mdv2008.0
+ Revision: 42128
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.11-8mdv2008.0
+ Revision: 22686
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.11-7mdv2007.0
+ Revision: 90970
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.11-6mdv2007.1
+ Revision: 74081
- rebuild for new vdr
- Import vdr-plugin-screenshot

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.11-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.11-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.11-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.11-2mdv2007.0
- rebuild for new vdr

* Tue Jun 27 2006 Anssi Hannula <anssi@mandriva.org> 0.0.11-1mdv2007.0
- 0.0.11

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.0.10-2mdv2007.0
- rebuild for new vdr

* Tue Jun 06 2006 Anssi Hannula <anssi@mandriva.org> 0.0.10-1mdv2007.0
- initial Mandriva release

