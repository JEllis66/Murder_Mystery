package com.LancastersTheater.models;


import java.util.Date;
import java.util.List;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.PrePersist;
import javax.persistence.PreUpdate;
import javax.persistence.Table;
import javax.persistence.Transient;
import javax.validation.constraints.Email;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.Size;

import org.springframework.format.annotation.DateTimeFormat;

@Entity
@Table(name="users")
public class User {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private long id;
	
	@NotEmpty(message="Name is required")
	@Size(min = 3, max = 64, message="Name must be between 3 and 64 characters")
	private String name;
	
	@NotEmpty(message="Email is required")
	@Email(message="Please enter a valid email address")
	private String email;

	@NotEmpty(message="Password is required")
	@Size(min = 8, max = 64, message="Password must be at 8 to 64 characters in length" )
	private String password;
	
	@Transient
	@NotEmpty(message="Password Confirmation is required")
	@Size(min = 8, max = 256, message="Password confirmation must be at 8 to 256 characters in length" )
	private String confirmation;
	
	@Column(updatable = false)
	@DateTimeFormat(pattern="yyyy-MM-dd")
    private Date createdAt;
    @DateTimeFormat(pattern="yyyy-MM-dd")
    private Date updatedAt;
    
    @PrePersist
    protected void onCreate() {
    	this.createdAt = new Date();
    }
    
    @PreUpdate
    protected void onUpdate() {
    	this.updatedAt = new Date();
    }
    
    @OneToMany(mappedBy="user", fetch = FetchType.LAZY)
    private List<Character> characterInformation;
    
    public User() {
    }

	public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
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

	public String getConfirmation() {
		return confirmation;
	}

	public void setConfirmation(String confirmation) {
		this.confirmation = confirmation;
	}

	public Date getCreatedAt() {
		return createdAt;
	}

	public void setCreatedAt(Date createdAt) {
		this.createdAt = createdAt;
	}

	public Date getUpdatedAt() {
		return updatedAt;
	}

	public void setUpdatedAt(Date updatedAt) {
		this.updatedAt = updatedAt;
	}

	public List<Character> getCharacterInformation() {
		return characterInformation;
	}

	public void setCharacterInformation(List<Character> characterInformation) {
		this.characterInformation = characterInformation;
	}
    
    
	
	

}
