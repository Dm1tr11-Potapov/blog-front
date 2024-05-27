<template>
    <header class="post-header">
        <h1 class="item-header">MY BLOG </h1>   
        <div id="div_top_hypers">
            <ul id="ul_top_hypers">
                <li class="li_top_hypers"> HOME</li>
                <li class="li_top_hypers"> FEED</li>
                <li class="li_top_hypers"> TIPS</li>
                <li class="li_top_hypers"> ABOUT</li>
                <li class="li_top_hypers"> SUBSCRIBE</li>
            </ul>
        </div>
    </header>
</template>

<script>
    export default {
        props: {
            PostHeader: Object}
    }
</script>

<style scoped>
body {
    background-color: rgb(255, 255, 255);
    padding: 0px;
    margin: 0px; 
    font-family: Verdana, Geneva, Tahoma, sans-serif;
}
.item-header {
    background-color: rgb(249,219,121);    
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    font-size: 40px;
    text-align: center;
    display: grid;
    align-items: center;
    color:rgb(47,46,46);       
    margin: 0 auto;
    height: 100px;
}

#div_top_hypers {
    background-color: rgb(47,46,46);
    color:rgb(249,219,121);
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    text-align: center;
    display: grid;
    align-items: center;
    margin: 0 auto;
    height: 65px;
}

#ul_top_hypers li{
    display: inline;
    padding-left: 25px;
    padding-right: 25px;
    margin: 0 auto;
    font-size: 24px;
    font-weight: 500;
    font-stretch:semi-condensed;
}
</style>


