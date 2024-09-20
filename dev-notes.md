# Developer's Notes
This are notes relevant for the developing of this project. They may include:

- References to underlying tech stack 
- Code snippets
- Note on important development decision

> Do not include secrets or any provite information

## Copier

We use Copier for project templating.

```shell
# create template with the latest changes to templating files
copier copy --vcs-ref HEAD ~/devel/Softare-Templates/ ./demo
```

```shell
# pass file to template
copier copy --vcs-ref HEAD --data-file ./Software-Templates/demo/smp.yml ./Software-Templates ./demo
```

Update anwers to template
- template must be versioned with Git tags
- rendered template must be vrsion with Git

Need to be discussed:

- We can control the output of SMP implementation in docassemble it selft. Robert is doing this. 
- CLI template, might not be necessary to create a new CLI
- Do we enforce the use of Git for version control?
    - update functionality is restricted to that.
- Follow up:
    - Get updates from WP1 (what changes are planing to do when) [Manuel]
        - Shall we include zenodo and similar integrations?
    - Look in to integration of Git/GitHub for validity tool [Angelina]
        - [Manuel] list of things that can potencially be implemented as automatic issues.
            - create cff file for software (but only for)
    - Idea: can we implement a gitHub bot? It will depend how far we can go.
    - Next meeting: Send meeting for Tuesday 11:00
    - Validation tool for CCF files: 
        - https://github.com/citation-file-format/citation-file-format?tab=readme-ov-file#validation-heavy_check_mark
        - https://pypi.org/project/cffconvert/
    - Holidays:     
        - Angelina
        - Robert

About Templates for R Language

- Possible management issues may arise because TAGs are used by copier to version  a template.
- Guide to organize R packages: https://r-pkgs.org/
- Popular package for templating: https://github.com/r-lib/usethis 
