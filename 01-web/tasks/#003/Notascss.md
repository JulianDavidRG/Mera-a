###
property: value;
h1 p{
    color:red
    font-size: 42px;
}
### Class selector
<class=intro> ºººcon "." es una clase ººº con ## es para un id
.intro{
    background:yellow;
}

### Selector
#intro{
    backgroud: yellow;
}

style inherintance
header{
    color: red;
    font-size: 24px;
}

.intro{
    font-family: Arial; tipo letra
    font-style:italic;
    color: #47759 or rgb(71, 144, 155)
    font-size: 32px; talla
    font-wight: bold (100-900);
}
text-trasform
.intro{
    text-trasform: uppercase;
    text-decoration: underline or line-through;
}

.outro{
    text-trasformation: capitalize;
}

### text shadow
h1{
    text-shadow: 3px(horizontal) 2px(vertical) 3px(blur radium) red;
}
### Multiples shadow
h1{
    text-shadow: 3px 2px 3px red, 3px 2px 3px blue;
}
h1{
    text-align: center;
}
.intro{
    line-height: 1.8;
    letter-spacing: 3px;
    word-spacing: 3px;
}

### The box model  margin, border, padding, content.
MARGIN PADDING AND BORDER 
class=box
p{
    margin: 5px top 10px R 5px B 10px L;
    border: 3px solid black;
    padding: 5px 3px 5px 3px;
}
.box{
    border: 3px solid red;
    # width: 50%;
    height: 200px;
}
propiedades como box-sinzing: border-box;

Two styles of box

    .box1 {
    border: 3px solid red;
    padding: 10px 10px 10px 10px;
    margin: 5px 5px 5px 5px;
    width: 200px;
    height: 100px;
    }

    .box2 {
    border: 3px solid red;
    padding: 10px 10px 10px 10px;
    margin: 5px 5px 5px 5px;
    width: 200px;
    height: 100px;
    box-sizing: border-box;
    }

border style = dashed, solid, double, groove, ridge, inset, outset.
.box{
    border-top: 3px dashed green;
    border-bottom: 5px solid red;
    border-radius: 10px; 
}
box-sizing: border-box; para evitar muchos calculos en le ancho 

### position static !important; anula todos los positions

### Backgroud 
.box{
    background-color: red;
    height: 100px;
    padding: 10px;
}

For image 
.box{
    background-image: url(html);
    background-repeat: repeast-x;
    background-size: contaion or cover;
    background-position: (0,0); px % unidades o top, left...
    height: 100px;
    padding: 10px;
   
}
no-repeat
repeat-x
repeat-y
repeat








ul{
    list-style-type: lower-roman;
    list-style-position: inside;
    list-style-image: url(img);
}

ul{
    list-style: square outside none;
}

### link
a:link
a:visited
a:active
a:hover

text-decoration

### U untraked no esta registrado el archivo 
### M modiffied 
### D DEleted 
### R renamed
fonts.google.com

.tarjeta