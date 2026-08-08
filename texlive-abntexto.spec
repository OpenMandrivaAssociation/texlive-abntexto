%global tl_name abntexto
%global tl_revision 78949
%global tl_version 1.1

Name:		texlive-%{tl_name}
Version:	%{tl_version}
Release:	%{tl_revision}.2
Summary:	LaTeX class for formatting academic papers in ABNT standards
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/abntexto
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abntexto.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abntexto.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{version}

%description
This is a LaTeX class created for Brazilian students to facilitate the
use of standards from the Associacao Brasileira de Normas Tecnicas
(ABNT) in academic works like TCCs, dissertations, theses.

