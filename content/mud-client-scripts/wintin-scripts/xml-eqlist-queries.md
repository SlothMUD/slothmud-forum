---
title: "XML eqlist queries"
topic_id: 1908
author: "Shiv"
date: 2006-05-30T21:10:44+00:00
last_activity: 2011-01-10T18:50:02+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 12
---

<div class="post" data-post-id="12801" data-author="Shiv" data-date="2006-05-30T21:10:44+00:00">

Hey all,

I made a change to my xml.php file in the eqlist directory so that it can be queried for a specific item name, and will return the results as an XML set.

The full path is http://www.slothmud.org/eqlist/xml.php?eqname={item name}

If someone out there in scripting land can figure out how to query it from within .net without using a browser, and to then parse the results and display them in a logical manner in a wintin.net window, I'd be very grateful-- and I imagine a lot of other people would be, too!

Thanks,

-Shiv/Enea

</div>

<div class="post" data-post-id="12810" data-author="Frobisher" data-date="2006-05-31T15:24:30+00:00">

Here's a script that will work with Wintin 2.x - it needs C# scripting which isn't available in v1.

To use the script, right click in the Script Manager and create a new alias. Call it eqlist or anything else you want. Copy and paste the text below into the alias properties box, and select C# as the script language.

With the alias defined, you can say for example 'eqlist diamond' to get a list of all the diamond thingies.

For the time being this is pointing at the backup eq list as there is a problem with the slothmud one. Just change the url in the listing below when Shiv has fixed the problem.

[code:1byr8p9k] Editor's Note: the problem has been fixed.

[/code:1byr8p9k]

regards

Fro

[code:1byr8p9k]

using System;

using System.Windows.Forms;

using System.Xml;

using System.IO;

using System.Net;

using ScriptEngine;

//css_reference ScriptEngine.dll;

public class Script : WintinScript

{

	public override void Init()

	{

		string line = wintin.Line.Trim();

		string url = "http://www.slothmud.org/eqlist/xml.php?eqname=" + line;

		WebRequest req; 

		Stream st = null;

		XmlTextReader xr = null;

			

		try

		{

			req = WebRequest.Create(url);

			WebResponse resp = req.GetResponse();

			st = resp.GetResponseStream();

			xr = new XmlTextReader(st);

			string eqname, type, armor, affects, res; 

			while(xr.Read())

			{

				xr.MoveToElement();

				if(xr.Name == "eq" && xr.NodeType == XmlNodeType.Element)

				{

					eqname = "";

					type = "";

					armor = "";

					affects = "";

					do

					{

						xr.Read();

						if(xr.NodeType == XmlNodeType.Element)

						{

							if(xr.Name == "eqname")

								eqname = xr.ReadElementString();

							if(xr.Name == "type")

								type = xr.ReadElementString();

							if(xr.Name == "armor")

								armor = xr.ReadElementString();

							if(xr.Name == "affects")

								affects = xr.ReadElementString();

						}

					}

					while(xr.Name != "eq" || xr.NodeType != XmlNodeType.EndElement);

	

					res = eqname + " (" + type + ") " + armor + " " + affects + "\r\n";

					wintin.SendToScreen(res);

				}

			}

		}

		catch(Exception ex)

		{

			MessageBox.Show(ex.Message);

		}

		finally

		{

			if(st != null)

				st.Close();

			if(xr != null)

				xr.Close();

		}

	}

}[/code:1byr8p9k]

</div>

<div class="post" data-post-id="12811" data-author="12345" data-date="2006-05-31T15:31:41+00:00">

Impressive.

</div>

<div class="post" data-post-id="12814" data-author="Shiv" data-date="2006-05-31T16:50:47+00:00">

It should be

[http://www.slothmud.org/eqlist/xml.php?eqname=](http://www.slothmud.org/eqlist/xml.php?eqname=)

not

[http://www.slothmud.org/xml.php?eqname=](http://www.slothmud.org/xml.php?eqname=)

-Shiv

</div>

<div class="post" data-post-id="12958" data-author="Shiv" data-date="2006-06-10T13:00:52+00:00">

Hi everyone,

Since the mud was down I took some time and wrote another xml tool.  This one is used to get the forge/brew/etc item about an info.  It's at:

<http://www.slothmud.org/eqlist/forgexml.php?eqname=(your item name here)>

Once again I'll let somone else write the client-side script for it, but it's a pretty easy tool to use.  For best results to see what it looks like, open it in IE, since IE has that neato built-in xml viewing tool... I keep hoping a coming version of Firefox will have something similar...

-Shiv/Enea

</div>

<div class="post" data-post-id="12981" data-author="Avatar" data-date="2006-06-12T13:57:37+00:00">

That's pretty nice, both of the web-based query tools.  

I've been considering keeping my forge notes scripted in the client, instead of my current setup = bunches of txt files and an excel spreadsheet.  Now it would be possible to integrate the two.  I could import the list of forge ingredients and flag each one as it pops.

I'll have to think of the benefits, but these new tools create interesting possibilities.

</div>

<div class="post" data-post-id="12987" data-author="Mannu" data-date="2006-06-13T22:49:09+00:00">

I'd love to use those scripts, but I'm logged on through a socks proxy.  It seems like the connection to the website cannot be made.  Is there a way to make it work with proxy connections?

</div>

<div class="post" data-post-id="32301" data-author="Vekna" data-date="2011-01-09T09:13:00+00:00">

Hi, immortals! Any chances to return "old" xml interface of eqlist?

</div>

<div class="post" data-post-id="32302" data-author="*Breeze*" data-date="2011-01-09T10:51:37+00:00">

sorry but no time soon because if i do that, 

it will be limited to 10 or so results per search

and people will complain that is not enough 

so

then someone will ask for filters

then someone will ask for more filters

then someone will ask me to change the format of the xml output

then someone will want a way to choose between the different xml outputs

... it never ends ..

its the same thing i went through with the html eqlist

like recently when Chobbs asked what people like about the MUD and someone brought up the eqlist how it was 'lacking' something to tell you what components go to what forges... that wasn't even what he asked..

anyways to be honest I don't have the time nor desire to mess with it at the moment

I would do a complete export weekly or so in xml format which could be downloaded and parsed by the clients but on the old eqlist when i did that people just linked to it directly instead of caching it which caused a ton of traffic since some moron(s) had it automatically look up every item he(they) saw, which downloaded a huge xml file each time.

so you see, not to rant too much but there is really no feasible way to do it at the moment.

</div>

<div class="post" data-post-id="32304" data-author="Vekna" data-date="2011-01-09T18:50:05+00:00">

> ***Benq* wrote:**
> I would do a complete export weekly or so in xml format which could be downloaded and parsed by the clients but on the old eqlist when i did that people just linked to it directly instead of caching it which caused a ton of traffic since some moron(s) had it automatically look up every item he(they) saw, which downloaded a huge xml file each time..

It will be great!  :)

</div>

<div class="post" data-post-id="32305" data-author="Tuck" data-date="2011-01-10T18:32:31+00:00">

> ***Benq* wrote:**
> I would do a complete export weekly or so in xml format which could be downloaded and parsed by the clients but on the old eqlist when i did that people just linked to it directly instead of caching it which caused a ton of traffic since some moron(s) had it automatically look up every item he(they) saw, which downloaded a huge xml file each time.

You can ban morons by IP, even make it automatically.

</div>

<div class="post" data-post-id="32306" data-author="*Breeze*" data-date="2011-01-10T18:50:02+00:00">

yeah that would be the first thing i work on before doing the actual output.

</div>
