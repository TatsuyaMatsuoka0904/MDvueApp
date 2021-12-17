<template>
	<div class="main-page">
        <div class="left-menu">
        
            <div class="note" v-for="note in noteList" v-bind:key="note.id">
                <div class="note-icon">
                    <i class="fas fa-file-alt"></i>
                </div>
                <div class="note-name">
                    {{ note.name }}
                </div>
            </div>

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
            })
        }
    }
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
.note {
    margin: 10px 0;
    display: flex;
    align-items: center;
    padding: 5px;
    color: rgba(25, 23, 17, 0.6);
}
.note-icon {
    margin-left: 10px;
}
.note-name {
    width: 100%;
    padding: 3px 10px;
}

</style>

