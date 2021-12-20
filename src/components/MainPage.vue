<template>
	<div class="main-page">
        <div @click.self="onEditNoteEnd()" class="left-menu">
            <draggable v-bind:list="noteList" group="notes">
            <NoteItem
             v-for="note in noteList"
             v-bind:note="note"
             v-bind:layer="1"
             v-bind:key="note.id"
             @delete="onDeleteNote"
             @select="onSelectNote"
             @editStart="onEditNoteStart"
             @editEnd="onEditNoteEnd"
             @addChild="onAddChildNote"
             @addNoteAfter="onAddNoteAfter"
            />
            </draggable>

            <button @click="onClickButtonAdd" class="transparent">
                <i class="fas fa-plus-square"></i>ノートを追加
            </button>
        </div>

        <div @click.self="onEditNoteEnd()" class="right-view">
            <template v-if="selectedNote == null">
                <div class="no-selected-note">ノートを選択してください</div>
            </template>
            <template v-else>
                <div class="path">
                    <small>{{ selectedPath }}</small>
                </div>
                <div class="note-content">
                    <h3 class="note-title">
                        {{ selectedNote.name }}
                    </h3>
                    <WidgetItem
                    v-for="widget in selectedNote.widgetList"
                    v-bind:widget="widget"
                    v-bind:layer="1"
                    v-bind:key="widget.id"
                    @delete="onDeleteWidget"
                    @addChild="onAddChildWidget"
                    @addWidgetAfter="onAddWidgetAfter"
                    />
                    <button class="transparent" @click="onClickButtonAddWidget">
                        <i class="fas fa-plus-square"></i>ウィジェットを追加
                    </button>
                </div>
            </template>
        </div>
    </div>
</template>


<script>
import NoteItem from './parts/NoteItem.vue'
import draggable from 'vuedraggable'
import WidgetItem from './parts/WidgetItem.vue'

export default {
	data() {
        return{
            noteList: [],
            selectedNote : null,
        }
    },
    methods: {

        onAddNoteCommom(targetList,layer,index) {
            layer = layer || 1
            const widget = {
                id : new Date().getTime().toString(16),
                type : 'heading',
                text : '',
                mouseover : false,
                children : [],
                layer : layer,
                widgetList : [],
            }
            // this.onAddWidgetCommon(note.widgetList);
            if (index == null){
                targetList.push(widget)
            } else {
                targetList.splice(index+1,0,widget)
            }
        },

        onAddWidgetCommon(targetList, layer, index){
            layer = layer || 1
            const widget = {
                id : new Date().getTime().toString(16),
                type : 'heading',
                text : '',
                mouseover : false,
                children : [],
                layer : layer,
            }
            if (index == null){
                targetList.push(widget)
            } else {
                targetList.splice(index+1, 0, widget)
            }
        },


        onClickButtonAddWidget() {
            this.onAddWidgetCommon(this.selectedNote.widgetList)
        },
        onAddChildWidget(widget){
            this.onAddWidgetCommon(widget.children, widget.layer + 1)
        },
        onAddWidgetAfter(parentWidget, note){
            const targetList = parentWidget == null ? this.selectedNote.widgetList : parentWidget.children
            const layer = parentWidget == null ? null: parentWidget.layer + 1
            const index = targetList.indexOf(note)
            this.onAddWidgetCommon(targetList, layer, index)
        },
        onDeleteWidget(parentWidget,widget){
            const targetList = parentWidget == null ? this.selectedNote.widgetList : parentWidget.children
            const index = targetList.indexOf(widget)
            targetList.splice(index,1)
        },


        
        onClickButtonAdd(){
            this.onAddNoteCommom(this.noteList)
        },
        onDeleteNote(parentNote,note){
            const targetList = parentNote == null ? this.noteList : parentNote.children
            const index = targetList.indexOf(note)
            targetList.splice(index,1)
        },
        onSelectNote(targetNote) {
            const updateSelectStatus = function(targetNote,noteList) {
                for (let note of noteList ) {
                    note.selected = (note.id === targetNote.id)
                    updateSelectStatus(targetNote, note.children)
                }
            }
            updateSelectStatus(targetNote,this.noteList)
            this.selectedNote = targetNote
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
        },
    },

    computed: {
        selectedPath(){
            const searchSelectedPath = function(noteList,path) {
                for (let note of noteList ) {
                    const currentPath = path == null ? note.name : `${path} / ${note.name}`
                    if (note.selected) return currentPath
                    const selectedPath = searchSelectedPath(note.children, currentPath)
                    if (selectedPath.length > 0) return selectedPath
                }
                return ''
            }
            return searchSelectedPath(this.noteList)
        }
    },

    components:{
        NoteItem,
        draggable,
        WidgetItem
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
.no-selected-note {
    text-align: center;
    font-size: 20px;
    margin: 20px;
}
.path {
    text-align: left;
    margin-bottom: 50px;      
}
.note-content {
    max-width: 900px;
    margin: 0 auto;
    text-align: left;
}
.note-title {
    margin-bottom: 15px;
}


</style>

