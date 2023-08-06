## [doc on github.io](https://walkerever.github.io/)


# json2html
show JSON in HTML.  rows sampling, collapse/expand, etc.

----

## Installation
   - pip install json_to_html 
   - run : "json2html" or "python -mjson2html"

----

## Examples

<pre>[yonghang@W5202860 json2html]$ curl -s walkerever.com/share/test/json/s6.json | qic
{
  <font color="#008700"><b>&quot;users&quot;</b></font>: [
    {
      <font color="#008700"><b>&quot;userId&quot;</b></font>: <font color="#626262">1</font>,
      <font color="#008700"><b>&quot;firstName&quot;</b></font>: <font color="#AF0000">&quot;Krish&quot;</font>,
      <font color="#008700"><b>&quot;lastName&quot;</b></font>: <font color="#AF0000">&quot;Lee&quot;</font>,
      <font color="#008700"><b>&quot;phoneNumber&quot;</b></font>: <font color="#AF0000">&quot;123456&quot;</font>,
      <font color="#008700"><b>&quot;emailAddress&quot;</b></font>: <font color="#AF0000">&quot;krish.lee@learningcontainer.com&quot;</font>
    },
    {
      <font color="#008700"><b>&quot;userId&quot;</b></font>: <font color="#626262">2</font>,
      <font color="#008700"><b>&quot;firstName&quot;</b></font>: <font color="#AF0000">&quot;racks&quot;</font>,
      <font color="#008700"><b>&quot;lastName&quot;</b></font>: <font color="#AF0000">&quot;jacson&quot;</font>,
      <font color="#008700"><b>&quot;phoneNumber&quot;</b></font>: <font color="#AF0000">&quot;123456&quot;</font>,
      <font color="#008700"><b>&quot;emailAddress&quot;</b></font>: <font color="#AF0000">&quot;racks.jacson@learningcontainer.com&quot;</font>
    },
    {
      <font color="#008700"><b>&quot;userId&quot;</b></font>: <font color="#626262">3</font>,
      <font color="#008700"><b>&quot;firstName&quot;</b></font>: <font color="#AF0000">&quot;denial&quot;</font>,
      <font color="#008700"><b>&quot;lastName&quot;</b></font>: <font color="#AF0000">&quot;roast&quot;</font>,
      <font color="#008700"><b>&quot;phoneNumber&quot;</b></font>: <font color="#AF0000">&quot;33333333&quot;</font>,
      <font color="#008700"><b>&quot;emailAddress&quot;</b></font>: <font color="#AF0000">&quot;denial.roast@learningcontainer.com&quot;</font>
    },
    {
      <font color="#008700"><b>&quot;userId&quot;</b></font>: <font color="#626262">4</font>,
      <font color="#008700"><b>&quot;firstName&quot;</b></font>: <font color="#AF0000">&quot;devid&quot;</font>,
      <font color="#008700"><b>&quot;lastName&quot;</b></font>: <font color="#AF0000">&quot;neo&quot;</font>,
      <font color="#008700"><b>&quot;phoneNumber&quot;</b></font>: <font color="#AF0000">&quot;222222222&quot;</font>,
      <font color="#008700"><b>&quot;emailAddress&quot;</b></font>: <font color="#AF0000">&quot;devid.neo@learningcontainer.com&quot;</font>
    },
    {
      <font color="#008700"><b>&quot;userId&quot;</b></font>: <font color="#626262">5</font>,
      <font color="#008700"><b>&quot;firstName&quot;</b></font>: <font color="#AF0000">&quot;jone&quot;</font>,
      <font color="#008700"><b>&quot;lastName&quot;</b></font>: <font color="#AF0000">&quot;mac&quot;</font>,
      <font color="#008700"><b>&quot;phoneNumber&quot;</b></font>: <font color="#AF0000">&quot;111111111&quot;</font>,
      <font color="#008700"><b>&quot;emailAddress&quot;</b></font>: <font color="#AF0000">&quot;jone.mac@learningcontainer.com&quot;</font>
    }
  ]
}

</pre>

----

###  conver to plain HTML

`[yonghang@W5202860 json2html]$ curl -s walkerever.com/share/test/json/s6.json | python -mjson2html`

<tt>
<table style="border-collapse:collapse;;" border=1 >
<tr class="child-bAyoMJvJfCiuoQyFqPXJ">
<td valign="top"><b>users</b></td>
    <td>
        <table style="border-collapse:collapse;;" border=1 width="100%">
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:#000000">
            <td valign="top"><b>userId</b></td>
            <td>1</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:#000000">
            <td valign="top"><b>firstName</b></td>
            <td>Krish</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:#000000">
            <td valign="top"><b>lastName</b></td>
            <td>Lee</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:#000000">
            <td valign="top"><b>phoneNumber</b></td>
            <td>123456</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:#000000">
            <td valign="top"><b>emailAddress</b></td>
            <td>krish.lee@learningcontainer.com</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:0F0F0F">
            <td valign="top"><b>userId</b></td>
            <td>2</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:0F0F0F">
            <td valign="top"><b>firstName</b></td>
            <td>racks</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:0F0F0F">
            <td valign="top"><b>lastName</b></td>
            <td>jacson</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:0F0F0F">
            <td valign="top"><b>phoneNumber</b></td>
            <td>123456</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:0F0F0F">
            <td valign="top"><b>emailAddress</b></td>
            <td>racks.jacson@learningcontainer.com</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:#000000">
            <td valign="top"><b>userId</b></td>
            <td>3</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:#000000">
            <td valign="top"><b>firstName</b></td>
            <td>denial</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:#000000">
            <td valign="top"><b>lastName</b></td>
            <td>roast</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:#000000">
            <td valign="top"><b>phoneNumber</b></td>
            <td>33333333</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:#000000">
            <td valign="top"><b>emailAddress</b></td>
            <td>denial.roast@learningcontainer.com</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:0F0F0F">
            <td valign="top"><b>userId</b></td>
            <td>4</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:0F0F0F">
            <td valign="top"><b>firstName</b></td>
            <td>devid</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:0F0F0F">
            <td valign="top"><b>lastName</b></td>
            <td>neo</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:0F0F0F">
            <td valign="top"><b>phoneNumber</b></td>
            <td>222222222</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:0F0F0F">
            <td valign="top"><b>emailAddress</b></td>
            <td>devid.neo@learningcontainer.com</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:#000000">
            <td valign="top"><b>userId</b></td>
            <td>5</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:#000000">
            <td valign="top"><b>firstName</b></td>
            <td>jone</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:#000000">
            <td valign="top"><b>lastName</b></td>
            <td>mac</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:#000000">
            <td valign="top"><b>phoneNumber</b></td>
            <td>111111111</td>
        </tr>
        <tr class="child-cBSfPBIIqxIXwjzFNXOT" style="background-color:#000000">
            <td valign="top"><b>emailAddress</b></td>
            <td>jone.mac@learningcontainer.com</td>
        </tr>
        </table>

    </td>
</tr>
</table>


----

### with -Z option

`[yonghang@W5202860 json2html]$ curl -s walkerever.com/share/test/json/s6.json | python -mjson2html -Z`

<header>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script> 
<script type="text/javascript"> 
    $(document).ready(function () { 
        $('tr.parent') .css("cursor", "pointer") .attr("title", "Click to expand/collapse") .click(function () { 
            $(this).siblings('.child-' + this.id).toggle(); 
        }); 
        $('tr[@class^=child-]').hide().children('td'); 
    }); 
</script>
</header>

<tt>
<table style="border-collapse:collapse;;" border=1 bgcolor="#101010">
<tr class="parent" id="vsTUnNFtCwPwaGtcoVKZ" title="Click to expand/collapse" style="cursor: pointer;"> <td bgcolor="#000033">D(1)</td> </tr>
<tr class="child-vsTUnNFtCwPwaGtcoVKZ">
<td valign="top"><b>users</b></td>
    <td>
        <table style="border-collapse:collapse;;" border=1 width="100%">
        <tr class="parent" id="qsqXBwVoGoUUMMmqFbFi" title="Click to expand/collapse" style="cursor: pointer;"> <td bgcolor="#000033">L(5)</td> </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:#000000">
            <td valign="top"><b>userId</b></td>
            <td>1</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:#000000">
            <td valign="top"><b>firstName</b></td>
            <td>Krish</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:#000000">
            <td valign="top"><b>lastName</b></td>
            <td>Lee</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:#000000">
            <td valign="top"><b>phoneNumber</b></td>
            <td>123456</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:#000000">
            <td valign="top"><b>emailAddress</b></td>
            <td>krish.lee@learningcontainer.com</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:1F1F1F">
            <td valign="top"><b>userId</b></td>
            <td>2</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:1F1F1F">
            <td valign="top"><b>firstName</b></td>
            <td>racks</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:1F1F1F">
            <td valign="top"><b>lastName</b></td>
            <td>jacson</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:1F1F1F">
            <td valign="top"><b>phoneNumber</b></td>
            <td>123456</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:1F1F1F">
            <td valign="top"><b>emailAddress</b></td>
            <td>racks.jacson@learningcontainer.com</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:#000000">
            <td valign="top"><b>userId</b></td>
            <td>3</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:#000000">
            <td valign="top"><b>firstName</b></td>
            <td>denial</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:#000000">
            <td valign="top"><b>lastName</b></td>
            <td>roast</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:#000000">
            <td valign="top"><b>phoneNumber</b></td>
            <td>33333333</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:#000000">
            <td valign="top"><b>emailAddress</b></td>
            <td>denial.roast@learningcontainer.com</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:1F1F1F">
            <td valign="top"><b>userId</b></td>
            <td>4</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:1F1F1F">
            <td valign="top"><b>firstName</b></td>
            <td>devid</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:1F1F1F">
            <td valign="top"><b>lastName</b></td>
            <td>neo</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:1F1F1F">
            <td valign="top"><b>phoneNumber</b></td>
            <td>222222222</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:1F1F1F">
            <td valign="top"><b>emailAddress</b></td>
            <td>devid.neo@learningcontainer.com</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:#000000">
            <td valign="top"><b>userId</b></td>
            <td>5</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:#000000">
            <td valign="top"><b>firstName</b></td>
            <td>jone</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:#000000">
            <td valign="top"><b>lastName</b></td>
            <td>mac</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:#000000">
            <td valign="top"><b>phoneNumber</b></td>
            <td>111111111</td>
        </tr>
        <tr class="child-qsqXBwVoGoUUMMmqFbFi" style="background-color:#000000">
            <td valign="top"><b>emailAddress</b></td>
            <td>jone.mac@learningcontainer.com</td>
        </tr>
        </table>

    </td>
</tr>
</table>



  
