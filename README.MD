# curso python con clexo07
# comandos para mergear desde consola
Paso 1 Clone el repositorio o actualice su repositorio local con los últimos cambios.

- git pull origen principal

Paso 2 Cambie a la rama base de la solicitud de extracción.

- git checkout principal

Paso 3 Fusiona la rama de la cabeza con la rama base.

- git merge dev

Paso 4 Empuje los cambios.

- git push -u origin main


## Comandos para mergear desde consola  

```sh
git pull origin main
git checkout main
git merge dev
git push -u origin main

## Comandos para mergear desde consola 

### Opción 2: Agregar un botón de copiar con HTML  
Si el `README.md` se ve en plataformas que admiten HTML (como GitHub Pages), puedes usar esto:  

```markdown
## Comandos para mergear desde consola

<pre id="codigo">
git pull origin main
git checkout main
git merge dev
git push -u origin main
</pre>

<button onclick="copiarTexto()">📋 Copiar</button>

<script>
function copiarTexto() {
    const codigo = document.getElementById("codigo").innerText;
    navigator.clipboard.writeText(codigo).then(() => {
        alert("Texto copiado al portapapeles!");
    }).catch(err => {
        console.error("Error al copiar: ", err);
    });
}
</script>
