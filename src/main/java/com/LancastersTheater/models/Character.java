package com.LancastersTheater.models;

import java.util.Date;
import java.util.List;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.OneToMany;
import javax.persistence.PrePersist;
import javax.persistence.Table;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.Size;

import org.springframework.format.annotation.DateTimeFormat;

@Entity
@Table(name="characters")
public class Character {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private long id;
	
	
	@NotEmpty(message="Please Enter a name")
	@Size(min = 1, max = 32, message="Name must be at least 1 character long")
	private String name;
	
	@NotEmpty(message="Please Enter a character description")
	@Size(min = 1, max = 128, message="Character description must be at least 1 character long")
	private String characterDescription;
	
	@NotEmpty(message="Please Enter a relationship to Jerry Lancaster")
	@Size(min = 5, max = 128, message="Replationship description must be at least 5 characters long and no longer than 128 characters")
	private String relationship;
	
	@NotEmpty(message="Please Enter a potential motive for murdering Jerry Lancaster")
	@Size(min = 5, max = 128, message="Potential motive must be at least 5 characters long and no longer than 128 characters")
	private String motive;
	
	@Column(updatable=true)
	@OneToMany(mappedBy="storyBeats")
	private List<Story> stories;
	
	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name="user_id")
    private User user;
	
	@Column(updatable = false)
	@DateTimeFormat(pattern="yyyy-MM-dd")
    private Date createdAt;
    @DateTimeFormat(pattern="yyyy-MM-dd")
    private Date updatedAt;
    
	public Character() {
	}

	public Character(
			 String name, String characterDescription, String relationship, String motive, List<Story> stories, User user) {
		this.name = name;
		this.characterDescription = characterDescription;
		this.relationship = relationship;
		this.motive = motive;
		this.stories = stories;
		this.user = user;
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

	public String getCharacterDescription() {
		return characterDescription;
	}

	public void setCharacterDescription(String characterDescription) {
		this.characterDescription = characterDescription;
	}

	public String getRelationship() {
		return relationship;
	}

	public void setRelationship(String relationship) {
		this.relationship = relationship;
	}

	public String getMotive() {
		return motive;
	}

	public void setMotive(String motive) {
		this.motive = motive;
	}

	public List<Story> getStories() {
		return stories;
	}

	public void setStories(List<Story> stories) {
		this.stories = stories;
	}

	public User getUser() {
		return user;
	}

	public void setUser(User user) {
		this.user = user;
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
	
	

}