autocmd filetype python set makeprg=python
autocmd filetype python command! Run make day2.py ./day2.input
autocmd filetype python command! Test make day2.py ./day2.test
echo "Run: :Run      Test: :Test"

