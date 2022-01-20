import React from "react";
import { Container } from "react-bootstrap";

export default function Invoices() {
  return (
    <main>
    	<div class="applogo">Chirpy</div>
    	<div class="youravatar">
    		<a href="userpage"><img src="https://www.blexar.com/avatar.png" class="youravatarpic" alt="youravatar"/></a>
    	</div>
    	<form>
    	<div class="createpost">
    		<div class="form-group">
      			<textarea class="form-control" id="exampleTextarea" rows="4" placeholder="What are you chirping about?" maxlength="280"></textarea>
      			<div class="send"><button type="submit" class="btn btn-primary sendpost">Send</button></div>
    		</div>
    	</div>
    	</form>
    	<div class="oldpost createpost">
    		<div class="card border-primary mb-3">
    			<div class="card-body">
    				<div class="leftalign">
    					<img src="https://www.blexar.com/avatar.png" class="avatarpic"/>
    					<span class="username">User0012324324</span>
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
    					<span class="username">User0012324324</span>
    					<br/><br/>
    					<p class="card-text">Walking up and down the aisles for what seems like hours. Walking up and down the aisles for what seems like hours.</p>
    				</div>
  				</div>
  			</div>
  		</div>
    </main>
  );
}