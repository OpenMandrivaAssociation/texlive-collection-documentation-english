# revision 27471
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-documentation-english
Epoch:		1
Version:	20121030
Release:	12
Summary:	English documentation
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-documentation-english.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-FAQ-en
Requires:	texlive-MemoirChapStyles
Requires:	texlive-Type1fonts
Requires:	texlive-amslatex-primer
Requires:	texlive-around-the-bend
Requires:	texlive-ascii-chart
Requires:	texlive-components-of-TeX
Requires:	texlive-comprehensive
Requires:	texlive-dtxtut
Requires:	texlive-first-latex-doc
Requires:	texlive-gentle
Requires:	texlive-guide-to-latex
Requires:	texlive-happy4th
Requires:	texlive-impatient
Requires:	texlive-intro-scientific
Requires:	texlive-knuth
Requires:	texlive-l2tabu-english
Requires:	texlive-latex-course
Requires:	texlive-latex-doc-ptr
Requires:	texlive-latex-graphics-companion
Requires:	texlive-latex-veryshortguide
Requires:	texlive-latex-web-companion
Requires:	texlive-latex2e-help-texinfo
Requires:	texlive-latex4wp
Requires:	texlive-latexcheat
Requires:	texlive-latexfileinfo-pkgs
Requires:	texlive-lshort-english
Requires:	texlive-macros2e
Requires:	texlive-math-e
Requires:	texlive-mathmode
Requires:	texlive-memdesign
Requires:	texlive-metafont-beginners
Requires:	texlive-metapost-examples
Requires:	texlive-mil3
Requires:	texlive-patgen2-tutorial
Requires:	texlive-pictexsum
Requires:	texlive-plain-doc
Requires:	texlive-presentations-en
Requires:	texlive-pstricks-examples-en
Requires:	texlive-pstricks-tutorial
Requires:	texlive-simplified-latex
Requires:	texlive-svg-inkscape
Requires:	texlive-tabulars-e
Requires:	texlive-tamethebeast
Requires:	texlive-tds
Requires:	texlive-tex-font-errors-cheatsheet
Requires:	texlive-tex-overview
Requires:	texlive-tex-refs
Requires:	texlive-texbytopic
Requires:	texlive-titlepages
Requires:	texlive-tlc2
Requires:	texlive-visualfaq
Requires:	texlive-webguide
Requires:	texlive-xetexref
Requires:	texlive-collection-documentation-base

%description
TeXLive collection-documentation-english package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Tue Oct 30 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20121030-1
+ Revision: 821208
- Update to latest release.

* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120810-1
+ Revision: 813902
- Update to latest release.

* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780212
- Update to latest release.
- Import texlive-collection-documentation-english
- Import texlive-collection-documentation-english

