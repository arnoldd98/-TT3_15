import React from "react";
import { Container } from "react-bootstrap";

export default function Invoices() {
  return (
    <main>
    	<div class="applogo">Logo</div>
    	<div class="youravatar">
    		<a href="homepage"><img src="https://www.rawshorts.com/freeicons/wp-content/uploads/2017/01/blue_repicthousebase_1484336386-1.png" class="youravatarpic" alt="youravatar"/></a>
    	</div>
    	<div class="avatarmiddle">
    		<img src="https://www.blexar.com/avatar.png" class="youravatarpicbig" alt="youravatar"/>
    		<br/><br/>
    		<h3>@user010101</h3>
    	</div>
    	<form>
    	<div class="createpost">
    		<div class="form-group">
      			<textarea class="form-control" id="exampleTextarea" rows="5" placeholder="What are you thinking about?" maxlength="280"></textarea>
      			<div class="send"><button type="submit" class="btn btn-primary sendpost">Send</button></div>
    		</div>
    	</div>
    	</form>
    	<div class="oldpost createpost">
    		<div class="card border-primary mb-3">
    			<div class="card-body">
    				<div class="leftalign">
    					<img src="https://www.blexar.com/avatar.png" class="avatarpic"/>
    					<span class="username">user010101</span>
    					<br/><br/>
    					<p class="card-text">Walking up and down the aisles for what seems like hours. Walking up and down the aisles for what seems like hours.</p>
    				</div>
  				</div>
  			</div>
  		</div>
  		<div class="oldpost createpost">
    		<div class="card border-primary mb-3">
    			<div class="card-body">
    				<div class="leftalign">
    					<img src="https://www.blexar.com/avatar.png" class="avatarpic"/>
    					<span class="username">user010101</span>
    					<br/><br/>
    					<p class="card-text">Walking up and down the aisles for what seems like hours. Walking up and down the aisles for what seems like hours.</p>
    				</div>
  				</div>
  			</div>
  		</div>
    </main>
  );
}