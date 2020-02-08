# [rights]  Copyright 2020 brianddk at github https://github.com/brianddk
# [license] Apache 2.0 License https://www.apache.org/licenses/LICENSE-2.0
# [repo]    https://github.com/brianddk/pypaperwallet
# [btc]     BTC-b32: bc1qwc2203uym96u0nmq04pcgqfs9ldqz9l3mz8fpj
# [tipjar]  https://gist.github.com/brianddk/3ec16fbf1d008ea290b0

def bitaddress():
    return """
<!doctype html>
<html lang="en">

<head>
  <title>github / brianddk / pypaperwallet</title>
  <meta charset="utf-8">
</head>

<body>
  <div id="main">
    <div id="wallets">
      <div id="singlearea" class="walletarea">
        <div class="body">
          <table>
            <tr>
              <td>
                <div id="keyarea" class="keyarea">
                  <div class="public">
                    <div class="pubaddress">
                      <span class="label" id="singlelabelbitcoinaddress">Bitcoin Address (m/44'/0'/0'/0/0)</span>
                    </div>
                    <div id="qrcode_public" class="qrcode_public">
                      <img alt="spec" width="1320" height="1320" style="width: 132px; height: 132px;" src="pub.png" />
                    </div>
                    <div class="pubaddress">
                      <span class="output" id="btcaddress">__BTC__ADDRESS__</span>
                    </div>
                    <div id="singleshare">SHARE</div>
                  </div>
                  <div class="private">
                    <div class="privwif">
                      <span class="label" id="singlelabelprivatekey">WIF Private Key</span>
                    </div>
                    <div id="qrcode_private" class="qrcode_private">
                      <img alt="spec" width="1640" height="1640" style="width: 164px; height: 164px;" src="priv.png" />
                    </div>
                    <div class="privwif">
                      <span class="output" id="btcprivwif">__BTC__WIF__</span>
                    </div>
                    <div id="singlesecret">SECRET</div>
                  </div>
                </div>
              </td>
            </tr>
          </table>
          <table>
            <tr>
              <td>
                <div id="singlesafety">
                  <p id="singletip1"><b>A Bitcoin wallet</b> is as simple as a single pairing of a Bitcoin address with its corresponding Bitcoin private key. Such a wallet has been generated and is displayed above.</p>
                  <p id="singletip2"><b>To safeguard this wallet</b> you must retain this page or otherwise record the Bitcoin address and private key. It is important to make a backup copy of the private key and store it in a safe location, or transfer it to a different wallet. Treat a paper wallet like cash or a signed check.</p>
                  <p id="singletip3"><b>Claim the funds</b> in this wallet by importing either the WIF or the BIP39/44 seed into a web-wallet or software wallet, then sending the entire balance to a new wallet or exchange.  Many wallets will do this automatically for WIF imports and call the process a "sweep". Popular web-wallets with WIF import capabilities include <a href="https://coin.space/?network=bitcoin">coin.space</a> (Georgia, US), <a href="https://wallet.btc.com/">BTC.com</a> (Amsterdam, NL) or <a href="https://www.blockchain.com/wallet/">Blockchain.com</a> (London, GB). A popular software wallet with good import capabilities would be <a href="https://electrum.org">Electrum</a> (Berlin, DE). More wallet choices can be found on the <a href="https://bitcoin.org/en/choose-your-wallet?step=1">Bitcoin.org Wallet Chooser</a>. You will need a wallet that has either WIF import capabilities or offers BIP39 and BIP44 compatibility. If you begin to retain significant amounts of bitcoin, many users will choose to start using a hardware wallet such as Trezor (Prague, CZ) or Ledger (Paris, FR).</p>
                  <p id="singletip4"><b>Check your balance</b> by going to <a href="https://www.blockchain.com/explorer">Blockchain.com</a> (London, GB) or <a href="https://btc.com/">BTC.com</a> (Amsterdam, NL) and entering your Bitcoin address above.  Your funds are fully claimed when the balance in this bitcoin address reads zero.  Any funds left in this address will eventually be voided.</p>
                  <p id="singletip5"><b>Cash out your bitcoins</b> for USD by sending them to an exchange after you've imported the key detailed above. Two popular bitcoin exchanges are <a href="https://pro.coinbase.com/">Coinbase.com</a> (San Francisco, US) and <a href="https://gemini.com/exchange/">Gemini.com</a> (New York, US). A more complete list can be found on the <a href="https://bitcoin.org/en/exchanges">Bitcoin.org exchange chooser</a>.</p>
                  <p id="singletip6"><b>Void after 90 days</b>. Please note that the funds in this wallet need to either be spent to a new wallet or sent to an exchange in the next 90 days or they will be forfeit.</p>
                </div>
              </td>
            </tr>
          </table>
          <table>
            <tr>
              <td>
                <div id="keyarea_f" class="keyarea">
                  <div class="private">
                    <div class="privwif">
                      <span class="label" id="singlelabelprivatekey_f">BIP39/44 Seed</span>
                    </div>
                    <div id="qrcode_private_f" class="qrcode_private">
                      <img alt="spec" width="1640" height="1640" style="width: 164px; height: 164px;" src="seed.png" />
                    </div>
                    <div class="privwif">
                      <span class="output" id="btcprivwif_f">__BIP39_SEED_1OF2__</span>
                      <span class="output" id="btcprivwif_f2">__BIP39_SEED_2OF2__</span>
                    </div>
                    <div id="singlesecret_f">SECRET</div>
                  </div>
                </div>
              </td>
            </tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</body>

</html>
"""

def disclosure():
    return """
<!doctype html>
<html lang="en">

<head>
  <title>github / brianddk / pypaperwallet</title>
  <meta charset="utf-8">
</head>

<body>
  <div id="main">
    <div id="wallets">
      <div id="singlearea" class="walletarea">
        <div class="body">
          <table>
            <tr>
              <td>
                <div id="singlesafety">
                  <center><h1>Political Contribution Disclosure</h1></center>
                  <br/><p><b>Instructions: </b> For contributions valued below $200 the personal information below may be omitted.  In these cases please fill in "N/A" for information you wish to withhold.  Please ensure you <b>DO</b> fill out the estimated USD value of your contribution and ensure you sign the form below.</p>
                  <br/><p><b>Name:</b> _____________________________________________________________________________________</p>
                  <br/><p><b>Address:</b> ___________________________________________________________________________________</p>
                  <br/></p><p><b>City:</b> _______________________________________________ <b>State:</b> ___________ <b>Zip:</b> _________________</p>
                  <br/><p><b>Employer:</b> _________________________________________________________________________________</p>
                  <br/><p><b>Occupation:</b> ________________________________________________________________________________</p>
                  <p><b>*</b> Note: The above information is only required for contributions valued over $200 and may be omitted for contributions of smaller value</p>
                  <br/><p>An individual may contribute up to $2,800 per election, with the primary and general treated as separate elections. By submitting this contribution, I agree that the first $2,800 of a contribution will be designated for the primary election, and any additional amount up to $2,800 will be designated for the general election. For contributions made after the primary, the full amount of the contribution, up to $2,800, will be designated for the general election.</p>
                  <p>This contribution does not originate from PACs of any kind or federally-registered lobbyists.</p>
                  <p>Federal law prohibits corporations, labor unions, federal contractors and foreign nationals, except lawfully admitted permanent residents of the U.S., from contributing to political campains. By signing here, I certify that I am at least 18 years old, I am a U.S. citizen or lawfully admitted permanent resident of the U.S., and the funds I am donating are not being provided to me by another person or entity for the purpose of making this contribution. </p>
                  <br/><br/><br/><br/><p><b>Signature:</b> ________________________________________________________________________________</p>
                  <br/><br/><p><b>Contribution Estimated USD Value:</b> ___________________________________________________________</p>
                </div>
              </td>
            </tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</body>

</html>
"""

def style():
    return """
.more { background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAABx0RVh0U29mdHdhcmUAQWRvYmUgRmlyZXdvcmtzIENTNXG14zYAAAAWdEVYdENyZWF0aW9uIFRpbWUAMDEvMDIvMTLltnQyAAAB1UlEQVQ4jYWTS04bQRCGv3q0x8gMYJCwknCGLDgLVwiH4grhLFaUXdhkQ0A8pBg/FOLpnmbhMYzxRKlNS1Vdf/31V5XknGnb+eXJCBjzbzu9OLu+azu845Opysej4wHmshF4uJ2TUrb3CV0gIBAKRboC5C2vdkDE9fdty6/xDegvXz+NgDbFUejZ+PjDgExmtpxS9vYwMe5u5iyX8RRoa5Ic+C4qx9KUN1MGu4E618yqJ5axAp44KA7ZL3eYzp/HKdVIw7WK8d6BuDvcod9TQlBEIOXEdPlElSoUJabIIs4Z7h9yNDwgqOMayLXw7epHVIBggrsgspZPUBQyiCgugRQji7TAVDF1XB2TlQoOYCqovkmpopS9fcoiM3ue0rOCYf8IU8NklWxiiOQ3EPXtWagIqo6KYWYEc4IGvMViA6RrnCJKVS9B8ypRHG1YKNa0Ur+C+MPt/I2BKWVZUO4FgvQ47PcptEDF+T2Z8TiZUMWIyGtpd+Bze5VTSqP57O/4YG+AN/RXbSiPkwmL5z/be/L+mM4vT2JKeUW7EXD1erMz/Lo4u77f0K9DDhdA1XG11jh9vWBb99Z9gAg5QZ2hzpmUa0RSW4f/gqSY0s3Vz+tufEjvHS8Tg6BXC7qVbQAAAABJRU5ErkJggg==)
			no-repeat left center; width: 17px; height: 17px; display: inline-block; float: right; cursor: pointer; }
.less { background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAK6wAACusBgosNWgAAABx0RVh0U29mdHdhcmUAQWRvYmUgRmlyZXdvcmtzIENTNXG14zYAAAAWdEVYdENyZWF0aW9uIFRpbWUAMDEvMDIvMTLltnQyAAABuklEQVQ4ja2US25TQRBFT336OSEY5ESyBfEakNiLt0AW5S2QvQQxAiZIYBwSz/yByH7dxcB2bPMME+hJS/W5fetWVUtE8K/HfzdcXfdfqsr4onuGuRz4Jrdzcg6Gg9HfQYAxAqmlSMMlQJO5/oliE4AtQLcR++btZQ+wPVsvVXbTfXFGEMyWU9rVM0yMu/Gc5bJ+DdztxWcH3otKVzbPmyq5LnwfzSgEBMxlhqJEBFWVKKUgG66rur53oH7aOeWkUlJSRCBHZracssorlLXttHpCpzonaYukjmsiivDu08daAZIJ7oLIVg9BUQgQUVwSua5Z5AWmiqnj6pisVXAAU0F1J6WK0q6e024Fs4cplbXonFxgapisk00MkdiBqDd7oSKoOiqGmZHMSZrwPRYHIMfaKaKsyhI01oni6IaFYptSyiOIT27nOwaq5FyQrUAIC/nBhK+UErRSos55z4878CrneJyTnHOvquymf3mOb+hvy/jw+QuLh5/NORkORvsGrq77dc6xpr0RcH07y3oF8G04GN0f6HdEDhdA1XG1vXb6dsAa+3Z8AREiQwkoEeQoiBzocHDkf/wnvwC5IpRVsUDNUgAAAABJRU5ErkJggg==)
			no-repeat left center; width: 17px; height: 17px; display: inline-block; float: right; }
a { position: relative; z-index: 20; }
.right { text-align: right; }
.walletarea { border: 2px solid #009900; }
hr { margin: 20px 0; border-top: 2px dashed #008000; }
.keyarea { height: 110px; text-align: left; position: relative; padding: 5px; }
.keyarea .public { float: left; }
.keyarea .pubaddress { display: inline-block; height: 40px; padding: 0 0 0 10px; float: left; }
.keyarea .privwif { margin: 0;  float: right; text-align: right; padding: 0 20px 0 0; position: relative; }
.keyarea .label { font-weight: bold; }
.keyarea .output { display: block; font-family: monospace; font-size: 1.25em; }
.keyarea .qrcode_public { display: inline-block; float: left; }
.keyarea .qrcode_private { display: inline-block; position: relative; top: 28px; float: right; }
.pubkeyhex { word-wrap: break-word; }
body { font-family: Arial; }
body, html { height: 99%; }
.faqs ol { padding: 0 0 0 25px; }
.faqs li { padding: 3px 0; }
.question { padding: 10px 15px; text-align: left; cursor: pointer; }
.question:hover, .expandable:hover { color: #77777A; }
.answer { padding: 0 15px 10px 25px; text-align: left; font-size: 80%; }
.faq { border: 0; border-top: 2px solid #009900; }
.button { margin-left: 5px; margin-right: 5px; }
input[type=checkbox] { position: relative; z-index: 20; }

#wallets { clear: both; }
#btcaddress, #btcprivwif, #btcprivwif_f, #btcprivwif_f2, #detailaddress, #detailaddresscomp, #detailprivwif, #detailprivwifcomp { font-family: monospace; font-size: 1.25em; }
#seedpoolarea { }
#seedpooldisplay {  font-family: monospace; font-size: 1.25em; width: 640px; padding: 15px 5px; word-wrap: break-word; }
.seedpoint { width: 6px; height: 6px; display: block; border-radius: 3px; background-color: #009900; position: absolute; z-index: 10; }
#generate { font-family: monospace; font-size: 1.25em; height: 305px; text-align: left; position: relative; padding: 5px; border: 2px solid #009900; clear: both; }
#generate span { padding: 5px 5px 0 5px; }
#generatekeyinput { position: relative; z-index: 20; }
#keyarea { height: 250px; }
#keyarea .pubaddress { float: none; display: block; padding: 0; height: auto; }
#keyarea .label { text-decoration: none; }
#keyarea .privwif { float: none; text-align: right; position: relative; padding: 0; }
#keyarea .qrcode_public { float: none; display: block; padding: 13px 11px 11px 11px; }
#keyarea .qrcode_private { float: none; display: block; top: 0; text-align: right; padding: 13px 11px 11px 11px; }
#singlearea { font-size: 90%; }
#singlesecret_f, #singlesecret { position: relative; top: -130px; float: right; right: 200px; color: red; font-weight: bolder; font-size: 200%;  }
#singleshare { position: relative; top: -110px; float: left; left: 160px; color: #009900; font-weight: bolder; font-size: 200%;  }
#singlesafety { text-align: left; padding: 5px; border-top: 2px solid #009900; top: -25px; position: relative; }

#keyarea_f { height: 250px; }
#keyarea_f .pubaddress { float: none; display: block; padding: 0; height: auto; }
#keyarea_f .label { text-decoration: none; }
#keyarea_f .privwif { float: none; text-align: right; position: relative; padding: 0; }
#keyarea_f .qrcode_public { float: none; display: block; padding: 13px 11px 11px 11px; }
#keyarea_f .qrcode_private { float: none; display: block; top: 0; text-align: right; padding: 13px 11px 11px 11px; }




#main { position: relative; text-align: center; margin: 0px auto; width: 808px; }
#logo { width: 578px; height: 80px; }
		
#paperarea { min-height: 120px; }
#paperarea .keyarea { border: 2px solid #009900; border-top: 0; }
#paperarea .keyarea.art { display: block; height: auto; border: 0; font-family: Ubuntu, Arial; padding: 0; margin: 0; }
#paperarea .artwallet .papersvg { width: 486px; height: 261px; border: 0; margin: 0; padding: 0; left: 0; }
#paperarea .artwallet .qrcode_public { top: 52px; left: 17px; z-index: 100; margin: 0; float: none; display: block; position: absolute; background-color: #FFFFFF; 
		                                padding: 5px 5px 2px 5px; } 
#paperarea .artwallet .qrcode_private { top: 104px; left: 360px; z-index: 100; margin: 0; float: none; display: block; position: absolute; background-color: #FFFFFF; 
		                                padding: 5px 5px 2px 5px; }
#paperarea .artwallet .btcaddress  
{
	position: absolute; top: 240px; left: 139px; z-index: 100; font-size: 10px; background-color: transparent;
	font-weight:bold; color: #000000; margin: 0;
		-webkit-transform-origin:top left; -webkit-transform:rotate(-90deg);
		-moz-transform-origin:top left;    -moz-transform:rotate(-90deg);
		-ms-transform-origin:top left;     -ms-transform:rotate(-90deg);
		-o-transform-origin:top left;      -o-transform:rotate(-90deg);
		transform-origin:top left;         transform:rotate(-90deg);
} 
#paperarea .artwallet .btcprivwif  
{
	position: absolute; top: 236px; left: 346px; z-index: 100; font-size: 7px; background-color: transparent;
	font-weight:bold; color: #000000; margin: 0;  
		-webkit-transform-origin:top left; -webkit-transform:rotate(-90deg);
		-moz-transform-origin:top left;    -moz-transform:rotate(-90deg);
		-ms-transform-origin:top left;     -ms-transform:rotate(-90deg);
		-o-transform-origin:top left;      -o-transform:rotate(-90deg);
		transform-origin:top left;         transform:rotate(-90deg);
}
#paperarea .artwallet .btcencryptedkey
{
	position: absolute; top: 174px; left: 332px; z-index: 100; font-size: 8px; background-color: transparent;
	font-weight:bold; color: #000000; margin: 0;  
		-webkit-transform-origin:top left; -webkit-transform:rotate(-90deg);
		-moz-transform-origin:top left;    -moz-transform:rotate(-90deg);
		-ms-transform-origin:top left;     -ms-transform:rotate(-90deg);
		-o-transform-origin:top left;      -o-transform:rotate(-90deg);
		transform-origin:top left;         transform:rotate(-90deg);
}
#bulkarea .body { padding: 5px 0 0 0; }
#bulkarea .format { font-style: italic; font-size: 90%; }
#bulktextarea { font-size: 90%; width: 98%; margin: 4px 0 0 0; }
#brainarea .keyarea { min-height: 110px; }
#brainview { margin-left: 5px; }
#detailkeyarea { padding: 10px; }
#detailarea { margin: 0; text-align: left; }
#detailarea .notes { text-align: left; font-size: 80%; padding: 0 0 20px 0; }
#detailarea .pubqr .item .label { text-decoration: none; }
#detailarea .pubqr .item { float: left; margin: 10px 0; position: relative; }
#detailarea .pubqr .item.right { float: right; position: relative; top: 0; } 
#detailarea .privqr .item .label { text-decoration: none; }
#detailarea .privqr .item { float: left; margin: 0; position: relative; }
#detailarea .privqr .item.right { float: right; position: relative; } 
#detailarea .item { margin: 10px 0; position: relative; font-size: 90%; padding: 1px 0; }
#detailarea .item.clear { clear: both; padding-top: 10px; }
#detailarea .label { display: block; font-weight: bold; }
#detailarea .output { display: block; font-family: monospace; font-size: 1.25em; }
#detailarea #detailqrcodepublic { position: relative; float: left; margin: 0 10px 0 0; padding: 13px 11px 11px 11px; }
#detailarea #detailqrcodepubliccomp { position: relative; float: right; margin: 0 0 0 10px; padding: 13px 11px 11px 11px; }
#detailarea #detailqrcodeprivate { position: relative; float: left; margin: 0 10px 0 0; padding: 13px 11px 11px 11px; }
#detailarea #detailqrcodeprivatecomp { position: relative; float: right; margin: 0 0 0 10px; padding: 13px 11px 11px 11px; }
#detailarea #detailqrcodeprivatebip38 { position: relative; margin: 0 10px 0 0; padding: 13px 11px 11px 11px; }
#detailpubkey { width: 590px; }
#detailbip38commands { padding-top: 5px; }
#detailbip38toggle { padding-top: 5px; }
#vanityarea { text-align: left; }
#vanityarea .label { text-decoration: underline; }
#vanityarea .output { font-family: monospace; font-size: 1.25em; display: block; }
#vanityarea .notes { text-align: left; font-size: 80%; padding: 0 0 20px 0; }
#vanitystep1area { text-align: left; position: relative; padding: 15px; border-bottom: 2px solid #009900; }
#vanitystep1label { padding-left: 5px; }
#vanitystep2area { border-top: 2px solid #009900; display: block; padding: 15px; }
#vanitystep2inputs { padding: 0 15px 10px 15px; }
#vanitycalc { margin-top: 5px; }

#splitarea { text-align: left; }
#splitarea span { padding: 0; }
#splitcommands { padding: 10px 15px; text-align: left; }
#combinecommands { padding: 10px 15px; }
#splitstep1area { text-align: left; position: relative; padding: 0; border-bottom: 2px solid #009900; }
.splitsharerow { border-bottom: 2px solid #009900; padding: 15px; }
.splitsharerow:last-child { border-bottom: 0; }
#combinelabelprivatekey { text-decoration: underline; }
#splitarea .output { display: block; font-family: monospace; font-size: 1.25em; }
#splitarea span.output { display: inline; }
#splitstep2area { padding:  10px 15px; }

.englishjson { text-align: center; padding: 40px 0 20px 0; }
.unittests { text-align: center; }
.unittests div { width: 894px; font-family: monospace; text-align: left; margin: auto; padding: 5px; border: 1px solid black; }
#testnet { background-color: Orange; color: #000000; border-radius: 5px; font-weight: bold; padding: 10px 0; margin: 0 auto 20px auto; }
#busyblock { position: fixed; background: url("data:image/gif;base64,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") #ccc no-repeat center; opacity: 0.4; width: 100%; height: 100%; top: 0; left: 0; z-index: 5000; }
#busyblock.busy { display: block; }
.hide { }
.show { display: block; }
		
@media screen 	
{
	#tagline { margin: 0 0 15px 0; font-style: italic; }
	.menu  
	{
	    text-align: left; margin: 0; padding: 0; display: block;
	    background-color: #009900; /* # 009900 # 53c100 */
	    border-top-left-radius: 5px; border-top-right-radius: 5px;
	}
	.menu .tab 
	{
	    position: relative; display: inline-block; border: 0px solid red;
	    margin: 0; list-style: none; z-index: 110; cursor: pointer; 
	    top: 1px; padding: 10px 20px; width: 162px; text-align: center;
	}
	.menu .tab.selected  
	{
	    cursor: default; 
	    background-color: #FFF; margin: 6px 16px; padding: 4px; border-radius: 5px; 
	}
	.menu .tab:hover  
	{
	    background-color: #FFF; margin: 6px 16px; padding: 4px; border-radius: 5px; 
	}
	.menu .tab.selected:hover { color: #000; }
	
    .pagebreak { height: 50px; }
	.commands { border-bottom: 2px solid #009900;  padding: 10px 2px; margin-bottom: 0; }
	.commands .row { padding: 0 0; text-align: left; } 
	.commands .row.extra { padding-top: 6px; }
	.commands span { padding: 0 10px; }
	.commands span.print { float: right; position: relative; z-index: 20; }
	.commands span.right { float: right; }
	.expandable { padding: 10px 15px; text-align: left; cursor: pointer; }

    #menu { visibility: visible; font-size: 90%; }
    #culturemenu { text-align: center; padding: 0 10px 5px 10px; margin-bottom: 3px; font-size: 90%; }
    #culturemenu span { padding: 3px; }
    #culturemenu .selected { text-decoration: none; color: #000000; }
    .culturemenurow { padding: 2px 0; }

	#braincommands .row .label { width: 200px; display: inline-block; }
	#braincommands .notes { font-size: 80%; display: block; padding: 5px 10px; }
	#brainpassphrase { width: 280px; position: relative; z-index: 20; }
	#brainpassphraseconfirm { width: 280px; position: relative; z-index: 20; }
    #brainpassphraseshow { position: relative; z-index: 20; }
    #brainview { position: relative; z-index: 20; }
	#brainwarning {  }
	#detailcommands { padding: 10px 0; }
	#detailcommands span { padding: 0 10px; }
	#detailprivkey { width: 460px; position: relative; z-index: 20; }
	#detailprivkeypassphrase { width: 250px; position: relative; z-index: 20; }
	#detailcommands .button { position: relative; z-index: 20; }
	#detailbip38encryptspan { }
	.paper .commands { border: 2px solid #009900; }
	#bulkstartindex, #paperlimit, #paperlimitperpage { width: 35px; } 
	#bulklimit { width: 45px; }
			
	.footer { font-size: 90%; clear: both; width: 770px; padding: 10px 0 10px 0; margin: 50px auto auto auto; }
	.footer div span.item { padding: 10px; }
	.footer .authorbtc { float: left; width: 470px; }
	.footer .authorbtc span.item { text-align: left; display: block; padding: 0 20px; }
	.footer .authorbtc div { position: relative; z-index: 100; }
	.footer .authorpgp { position: relative; }
	.footer .authorpgp span.item { text-align: right; display: block; padding: 0 20px; }
	.footer .copyright { font-size: 80%; clear: both; padding: 5px 0; }
	.footer .copyright span { padding: 10px 2px; }
    .footer .tooltip { text-align: left; border: 2px solid green; background-color: #FFFFF6; margin: 5px; padding: 10px; top: 0px; position: relative;  }
	.footer .statusgood { color: green; font-weight: bold; }
    .footer .statuswarn { color: orange; font-weight: bold; }
	.footer .statusbad { color: red; font-weight: bold; }
    .footer .statusicon { background-color: none; font-size: 120%; padding: 1px 2px; }
    .footer .statusicon:hover { background-color: green; cursor: pointer; }
}
@media print
{
	#main { width: auto; }
	#singlearea { border: 0; }
	#singlesafety { border: 0; }
	#paperarea .keyarea:first-child { border-top: 2px solid #009900; }
	#paperarea .keyarea.art:first-child { border: 0; }
	.pagebreak { height: 1px; }
	.paper #logo { }
	.menu, .footer, .commands, #tagline, #faqs, #culturemenu { }
	#detailprivwif { width: 285px; word-wrap: break-word; }
	#detailprivwifcomp { width: 310px; word-wrap: break-word; text-align: right; }
	#detailarea .privqr .item.right { width: 310px; }
	#detailarea .privqr .item { width: 285px; }
	#detailarea .notes { }
	#seedpoolarea { }
	.faq { }
}


table, th, td {  
  margin: 0;
  padding: 0;  
  border-spacing: 0;
}

table {
  width: 100%;
}
"""

def margins():
    return """
@page {
  size: letter; /* Change from the default size of A4 */
  margin: 0.25in; /* Set margin on each page */
}"""

