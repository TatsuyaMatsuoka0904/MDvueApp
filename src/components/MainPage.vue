<template>
	<div class="main-page">
        <div @click.self="onEditNoteEnd()" class="left-menu">

            <NoteItem
             v-for="note in noteList"
             v-bind:note="note"
             v-bind:layer="1"
             v-bind:key="note.id"
             @delete="onDeleteNote"
             @editStart="onEditNoteStart"
             @editEnd="onEditNoteEnd"
             @addChild="onAddChildNote"
             @addNoteAfter="onAddNoteAfter"
            />

            <button @click="onClickButtonAdd" class="transparent">
                <i class="fas fa-plus-square"></i>ノートを追加
            </button>
        </div>

        <div @click.self="onEditNoteEnd()" class="right-view">
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
        onAddNoteCommom(targetList,layer,index){
            layer = layer || 1
            const note = {
                id :new Date().getTime().toString(16),
                name : `NewNote-${layer}-${targetList.length}`,
                mouseover : false,
                editing : false,
                children : [],
                layer : layer,
            }
            if (index == null){
                targetList.push(note)
            } else {
                targetList.splice(index+1, 0, note);
            }
        },
        
        onClickButtonAdd(){
            this.onAddNoteCommom(this.noteList)
        },
        onDeleteNote(parentNote,note){
            const targetList = parentNote == null ? this.noteList : parentNote.children
            const index = targetList.indexOf(note)
            targetList.splice(index,1)
        },

        onEditNoteStart(editNote,parentNote) {
            const targetList = parentNote == null ? this.noteList : parentNote.children
            for (let note of targetList) {
                note.editing = (note.id === editNote.id)
                this.onEditNoteStart(editNote, note)
            }
        },
        onEditNoteEnd(parentNote){
            const targetList = parentNote == null ? this.noteList : parentNote.children
            for (let note of targetList) {
                note.editing = false
                this.onEditNoteEnd(note)
            }
        },

        onAddChildNote(note){
            this.onAddNoteCommom(note.children, note.layer+1)
        },
        onAddNoteAfter(parentNote,note) {
            const targetList = parentNote == null ? this.noteList :parentNote.children
            const layer = parentNote == null
            const index = targetList.indexOf(note)
            this.onAddNoteCommom(targetList,layer,index)
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

