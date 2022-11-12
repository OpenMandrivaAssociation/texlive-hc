Name:		texlive-hc
Version:	15878
Release:	1
Summary:	Replacement for the LaTeX classes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hc
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of replacements for the default LaTeX classes, based upon
the Koma-Script bundle and the seminar class. Includes hcart,
hcreport, hcletter, and hcslides.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/hc/hc-de.bst
%{_texmfdistdir}/bibtex/bst/hc/hc-en.bst
%{_texmfdistdir}/tex/latex/hc/german.hld
%{_texmfdistdir}/tex/latex/hc/hcart.cls
%{_texmfdistdir}/tex/latex/hc/hcletter.cls
%{_texmfdistdir}/tex/latex/hc/hcreport.cls
%{_texmfdistdir}/tex/latex/hc/hcslides.cls
%doc %{_texmfdistdir}/doc/latex/hc/COPYING
%doc %{_texmfdistdir}/doc/latex/hc/FILES
%doc %{_texmfdistdir}/doc/latex/hc/README
%doc %{_texmfdistdir}/doc/latex/hc/hc.ps
#- source
%doc %{_texmfdistdir}/source/latex/hc/hc.dtx
%doc %{_texmfdistdir}/source/latex/hc/hc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
