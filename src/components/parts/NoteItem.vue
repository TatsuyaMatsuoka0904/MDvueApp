<template>
<div class="note-family">
    <div class="note"
        @mouseover="onMouseOver"
        @mouseleave="onMouseLeave"
        @click="onSelect(note)"
        v-bind:class="{ mouseover: note.mouseover && !note.editing, selected: note.selected }"
    >
    <template v-if="note.editing">
        <input v-model="note.name" class="transparent" @keypress.enter="onEditEnd" />
    </template>
    <template v-else>
    <div class="note-icon">
        <i class="fas fa-file-alt"></i>
    </div>
    <div class="note-name">{{note.name}}</div>

    <div v-show="note.mouseover" class="buttons">
        <div v-if="layer < 3" @click="onClickChildNote(note)" class="button-icon">
            <i class="fas fa-sitemap"></i>
        </div>
        <div @click="onClickAddNoteAfter(parentNote, note)" class="butotn-icon">
            <i class="fas fa-plus-circle"></i>
        </div>
        <div @click="onClickEdit(note)" class="button-icon">
            <i class="fas fa-edit"></i>
        </div>
        <div @click="onClickDelete(parentNote,note)" class="button-icon">
            <i class="fas fa-trash"></i>
        </div>
    </div>
    </template>
    </div>
    <div class="child-note">
        <draggable v-bind:list="note.children" group="notes">
        <NoteItem
        v-for="childNote in note.children"
        v-bind:note="childNote"
        v-bind:layer="layer + 1"
        v-bind:parentNote="note"
        v-bind:key="childNote.id"
        @select="onSelect"
        @delete="onClickDelete"
        @editStart="onClickEdit"
        @editEnd="onEditEnd"
        @addChild="onClickChildNote"
        @addNoteAfter="onClickAddNoteAfter"
        />
        </draggable>
    </div>
</div>
</template>

<script>
import draggable from 'vuedraggable'

export default {
  name: 'NoteItem',
  props: [
    'note',
    'parentNote',
    'layer',
  ],
  components: {
      draggable
  },

  methods: {
      onMouseOver() {
          this.note.mouseover = true
      },
      onMouseLeave() {
          this.note.mouseover = false 
      },
      onSelect(note) {
          this.$emit('select',note)
      },
      onClickDelete(parentNote,note){
          this.$emit('delete', parentNote, note);
      },
      onClickEdit(note){
          this.$emit('editStart', note)
      },
      onEditEnd(){
          this.$emit('editEnd')
      },
      onClickChildNote(note){
          this.$emit('addChild', note)
      },
      onClickAddNoteAfter(parentNote,note) {
          this.$emit('addNoteAfter', parentNote,note)
      },
  }
  
}
</script>

<style scoped>
.note {
  margin: 10px 0;
  display: flex;
  align-items: center;
  padding: 5px;
  color: rgba(25, 23, 17, 0.6);
}
.mouseover {
    background-color: rgb(248, 218, 218);
    cursor: pointer;
}
.note-icon {
    margin-left: 10px;
}
.note-name {
    width: 100%;
    padding: 3px 10px;
}
.buttons {
    display: flex;
    flex-direction: row;
}
.button-icon {    
    padding: 3px;
    margin-left: 4px;
    border-radius: 5px;
}
.selected {
    color: black;
    background-color: rgb(232, 231, 228);
    font-weight: 600;
  }
.child-note {
    padding-left: 10px;
}

</style>
