autocmd filetype python set makeprg=python
autocmd filetype python command! Run make day1.py ./day1.input
autocmd filetype python command! Test make day1.py ./day1.test
echo "Run: :Run      Test: :Test"

