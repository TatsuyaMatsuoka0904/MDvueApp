<template>
    <div class="event-page">
        <h2>学習3：イベント</h2>

        <h3><span class="badge badge-secondary">Javascript</span></h3>
        <span id="countText">Clicked Button: 0 </span>
        <button id="button" class="btn btn-sm btn-info">+1</button>
        <br>
        <br>
        <h3><span class="badge badge-secondary">Vue.js</span></h3>
        <span>Clicked Button: {{ count }}</span>
        <button @click="onClickButton()" id="butoon" class="btn btn-sm btn-info">+1</button>
    </div>
</template>

<script>
let count = 0;
window.onload = function() {
    const button = document.getElementById('button');
    button.onclick = function() {
        count++;
        const countText = document.getElementById('countText');
        countText.innerHTML = 'Clicked Button: '+ count;
    };
}

export default {
    data() {
        return{
            count:0
        }
    },
    methods: {
        onClickButton() {
            this.count++
        }
    }
}
</script>

<style scoped>
.event-page {
    padding: 20px;
}
</style>