<template>
    <div class="pageContainer">
        <slot></slot>
    </div>
</template>

<script>
export default {
    name: 'PageComponent'
}
</script>

<style scoped>
    .pageContainer {
        padding: 3vw 5vw 10vw 5vw;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: auto;
    }
</style>