<template>       
    <footer class="post-footer">
        <div class="footer">
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe vel optio nostrum commodi. Vitae est maiores aut eveniet mollitia sint repellat, veniam aperiam iste alias. Sint ullam beatae vel facere.
        </div>        
    </footer>
</template>

<script>
    export default {
        props: {
            PostFooter: Object}
    }
</script>

<style scoped>
/* body {
    background-color: rgb(255, 255, 255);
    padding: 0px;
    margin: 0px; 
    font-family: Verdana, Geneva, Tahoma, sans-serif;
} */


.footer{
    background-color: rgb(47,46,46);
    color:rgb(255, 255, 255);
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    text-align: center;
    display: grid;
    align-items: center;
    margin: 0 auto;
    font-size: 20px;
    height: 150px;
    padding-left: 300px;
    padding-right: 300px;
}
</style>


