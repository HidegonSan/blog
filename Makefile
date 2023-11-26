.PHONY:
	server chroma papermod instantpage update debug-make-posts debug-delete-posts new-%

server:
	hugo server -D --disableFastRender --ignoreCache

chroma:
	hugo gen chromastyles --style=monokai > ./assets/css/chroma/chroma_dark.css
	hugo gen chromastyles --style=monokailight > ./assets/css/chroma/chroma_light.css
	sed -i 's/.chroma/.dark .chroma/g' ./assets/css/chroma/chroma_dark.css
	python chroma.py

submodule:
	git submodule update --remote --merge

goatcounter:
	curl https://gc.zgo.at/count.js -o ./assets/js/goatcounter.js

instantpage:
	git clone git@github.com:instantpage/instant.page.git tmp/instant.page && \
	cd ./tmp/instant.page && \
	npm install uglify-js && \
	npx --yes uglifyjs ./instantpage.js --compress --mangle --toplevel --output ./instantpage.min.js && \
	sed -i '1s/^/\n\/\*\n\n/' LICENSE && \
	echo -e "\n*/" >> LICENSE && \
	cat LICENSE >> ./instantpage.min.js && \
	cp ./instantpage.min.js ./../../assets/js/instantpage.js && \
	cd ./../../ && \
	rm -rf ./tmp

katex:
	mkdir tmp && \
	cd tmp && \
	curl -L https://github.com/KaTeX/KaTeX/releases/latest/download/katex.zip -o ./katex.zip && \
	unzip ./katex.zip && \
	cd ./katex && \
	cp ./fonts/* ./../../static/assets/css/fonts && \
	mkdir -p ./../../assets/js/katex/contrib && \
	mkdir -p ./../../assets/css/katex/ && \
	cp ./katex.min.js ./../../assets/js/katex/katex.min.js && \
	cp ./contrib/auto-render.min.js ./../../assets/js/katex/contrib/auto-render.min.js && \
	cp ./contrib/copy-tex.min.js ./../../assets/js/katex/contrib/copy-tex.min.js && \
	cp ./contrib/mhchem.min.js ./../../assets/js/katex/contrib/mhchem.min.js && \
	cp ./katex.min.css ./../../assets/css/katex/katex.min.css && \
	cd ./../../ && \
	rm -rf ./tmp

mermaid:
	curl https://cdn.jsdelivr.net/npm/mermaid@latest/dist/mermaid.min.js -o ./assets/js/mermaid.min.js

update: submodule goatcounter instantpage katex mermaid

debug-make-posts:
	for i in `seq 0 1 50`; do\
		hugo new posts/__test_$$i.md;\
	done

debug-delete-posts:
	for i in `seq 0 1 50`; do\
		rm ./content/posts/__test_$$i.md;\
	done

# Thanks: http://puni56.net/posts/makefile-arg/
new-%:
	hugo new posts/${@:new-%=%}/index.md
