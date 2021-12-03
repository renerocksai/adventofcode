autocmd filetype python set makeprg=python
autocmd filetype python command! Run make day3.py ./day3.input
autocmd filetype python command! Test make day3.py ./day3.test
echo "Run: :Run      Test: :Test"

