pandoc ^
-s C:\xampp\htdocs\convertor_md\convert\1.md C:\xampp\htdocs\convertor_md\convert\text.md ^
-o ../result/output1.docx ^
--lua-filter=../docx/luafilters.lua ^
--reference-doc=../docx/custom-reference.docx 
