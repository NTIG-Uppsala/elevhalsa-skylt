## Where to change hardcoded data

A carousel item found in index.html.
Anything wrapped with curly brackets can be changed.

```html
<div class="carousel-item active">
    <div class="name row justify-content-between">
        <div class="col-7">
            <--! Name -->
            <h2> {Name} </h2>
        </div>
        <div class="col">
            <--! Role -->
            <h2> {Role} </h2>
        </div>
    </div>
    <div class="row">
        <div class="col">
            <p>
                <--! Info -->
                {Info}
            </p>
        </div>
        <div class="col text-center">
            <--! Image -->
            <img class="profile-image" src="{Image source}" />
        </div>
    </div>
    <p class="contact">
        <--! Email -->
        E-post: {Email} <br />
        <--! Phone -->
        Telefon: {Phone} <br />
        <--! Working days and hours -->
        Arbetar: {Working days and hours}
    </p>
</div>
```