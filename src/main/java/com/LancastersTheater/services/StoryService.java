package com.LancastersTheater.services;


import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.validation.BindingResult;

import com.LancastersTheater.models.Character;
import com.LancastersTheater.models.Story;
import com.LancastersTheater.repositories.StoryRepository;

@Service
public class StoryService {

	@Autowired
	private StoryRepository storyRepository;
	
	
	//Create
	
		public Story createTeam(Character character) {
				Story s = new Story();
				s.setTitle("Story" + character.getStories().size());
				return storyRepository.save(s);
		}
	
	
	//Read
	
		public List<Story> allStories() {
			return storyRepository.findAll();
		}

		public Story findById(Long id) {
			Optional<Story> optionalStory = storyRepository.findById(id);
			if(optionalStory.isPresent()) {
				return optionalStory.get();
			}
			return null;
		}
		
		
	//Update
		
		public Story updateTeam(Story s) {
			return storyRepository.save(s);
		}
		
	//Delete
		
		public void deleteTeam(Long id) {
			storyRepository.delete(findById(id));
		}
		
	
}

