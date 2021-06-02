pandoc ^
-s 1.md 2.md ^
-o result/labs.docx ^
--lua-filter=docx/luafilters.lua ^
--reference-doc=docx/custom-reference.docx
