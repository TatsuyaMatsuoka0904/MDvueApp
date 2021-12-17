<template>
	<div class="main-page">
        <div class="left-menu">

            <NoteItem
             v-for="note in noteList"
             v-bind:note="note"
             v-bind:key="note.id"
            />

            <button @click="onClickButtonAdd" class="transparent">
                <i class="fas fa-plus-square"></i>ノートを追加
            </button>
        </div>

        <div class="right-view">
            右メニュー
        </div>
    </div>
</template>

<script>
import NoteItem from './parts/NoteItem.vue'

export default {
	data() {
        return{
            noteList: [],
        }
    },
    methods: {
        onClickButtonAdd(){
            this.noteList.push({
                id: new Date().getTime().toString(16),
                name : 'New Note',
                mouseover: false
            })
        }
    },
    components:{
        NoteItem
    },
}
</script>

<style scoped >
.main-page {
    display: flex;
    height: calc(100vh - 60px);
}
.left-menu {
    width: 350px;
    background-color:#f7f6f3;
}
.right-view {
    flex-grow: 1;    
    padding: 10px;
}
button.transparent {
    margin: 5px;
    background: transparent;
    border: none;
}


</style>

