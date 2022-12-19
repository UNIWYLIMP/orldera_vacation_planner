function showcase()
{
    show = document.getElementById('root')
    show.innerHTML = "<div class='showcase'> <video src='video.mp4' muted loop autoplay></video> <div class='text'> <div id='h11'><h1 class='first'>EXPERIENCE!</h1></div> </div> </div>"
    counter = 0;
    vn = setInterval(updater, 2000);
}

function updater()
{
    if (counter == 0)
    {
        hwl = document.getElementById('h11')
        hwl.innerHTML = "<h1 class='second'>THE WARM HOLIDAYS!</h1>"
        counter = 1;
    }

    else if (counter == 1)
    {
        hwl = document.getElementById('h11')
        hwl.innerHTML = "<h1 class='third'>ENJOY!</h1>"
        counter = 2;
    }

    else if (counter == 2)
    {
        hwl = document.getElementById('h11')
        hwl.innerHTML = "<h1 class='fouth'>CAUSE VACATION!</h1>"
        counter = 3;
    }

    else if (counter == 3)
    {
        hwl = document.getElementById('h11')
        hwl.innerHTML = "<h1 class='fifth'>IS HERE!</h1>"
        counter = 4;
    }

    else if (counter == 4)
    {
        hwl = document.getElementById('h11')
        hwl.innerHTML = "<h1 class='sixth'>JOURNEY WITH ORLDERA NOW!</h1>"
        counter = 5;
    }

    else if (counter == 5)
    {
        show = document.getElementById('root')
        show.innerHTML = "<div class='container-md px-1 px-md-2'><div class='row-6 pt-2 d-flex flex-row'><div class='col-6'><img src='./img/logo.png' class='imglogo'></div><div class='col-6 text-end'><p class='header'>ELIONA <img src='bdhd'></p></div></div><div class='row mt-0 pt-5 pt-lg-0 pb-lg-5 mb-2'><div class='row-6 d-block d-md-none'><div class='row w-50 mx-auto'><img src='home-font.png' class='nnn'></div></div><div class='col-12 col-md-4 my-auto text-center text-md-start'><div class='row mt-2 mt-md-0 pt-4'><h1 class='headings'>VACATION IS HERE!</h1></div><div class='row pt-3 px-1'><div class='animate_p'><p class='body'>Caleb Online Community, Share Experience, Thought, Ideas and Meet New People Around The Campus.</p></div></div><div><a href='signup.html' class='btn btn-dark mx-1'>SIGNUP</a><a href='login.html' class='btn btn-dark'>LOGIN</a></div></div><div class='col-6 d-none d-md-block'><div class='row '><img src='home-font.png' class='nnn'></div></div></div></div></div></div>"
        clearInterval(vn)
    }
}