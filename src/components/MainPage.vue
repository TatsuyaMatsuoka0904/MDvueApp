<template>
	<div class="main-page">
        <div class="left-menu">
            左メニュー
        </div>
        <div class="right-view">
            右メニュー
        </div>
    </div>
</template>

<script>
export default {
	
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

</style>

