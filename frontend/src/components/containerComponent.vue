<template>
        <div 
            class="message_list_container"
        >
            <slot></slot>
        </div>
</template>

<script>
export default {
    name: 'ContainerComponent'
}
</script>

<style scoped>
.message_list_container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    /* width: auto; */
    background-color: rgb(238, 238, 238);
    padding: 10px 10px 10px 10px;
    margin-top: 20px;
    border-radius: 5px;
    width: 100%;
}
</style>