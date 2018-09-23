from sphinx_theme import make

make.main(
    project_name='slext',
    force_rebuild=True,
    autodoc_generate=True,
    autodoc_force_override=True,
)
