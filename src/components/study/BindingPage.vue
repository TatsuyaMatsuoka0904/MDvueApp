<template>
    <div class="binding-page">
        <h2>学習１:双方向バインディング</h2>
        
        <h3><span class="badge badge-secondary">Text</span></h3>
        <input class="form-control" id="name" />
        <span id="text"></span>
        <br>
        <br>
        
        <h3><span class="badge badge-secondary">Vue.js</span></h3>
        <input v-model="name" class='form-control' >
        <span>{{ name }}</span>
    </div>
</template>

<script>
window.onload = function load () {
    const nameInput = document.getElementById('name');
    nameInput.oninput = function() {
        const name = nameInput.value;
        const text = document.getElementById('text');
        text.innerHTML = '入力された名前は' +  name + 'です';
    };
}

export default {
    data() {
        return{
            name : '',
        }
    }
}

</script>

<style scoped>
.binding-page {
    padding: 20px;
}

</style>