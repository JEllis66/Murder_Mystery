package com.LancastersTheater.models;

import javax.validation.constraints.Email;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.Size;

public class LoginUser {
	
	@NotEmpty(message="Please enter an email address")
	@Email(message="Please enter a valid email address")
	private String email;

	@NotEmpty(message="Please enter a password")
	@Size(min=8, max=32, message="Your login credentials do not match any account, please try again")
	private String password;
	
	public LoginUser() {
		
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}
	
}
