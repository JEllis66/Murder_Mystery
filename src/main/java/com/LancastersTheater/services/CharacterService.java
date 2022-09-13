package com.LancastersTheater.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.validation.BindingResult;

import com.LancastersTheater.models.Character;
import com.LancastersTheater.models.User;
import com.LancastersTheater.models.Story;
import com.LancastersTheater.repositories.CharacterRepository;

@Service
public class CharacterService {

	@Autowired
	private CharacterRepository characterRepository;
	
	
	//Create
	
		public Character createCharacter(Character b, User u) {
			b.setUser(u);
			return characterRepository.save(b);
		}
	
	
	//Read
	
		public List<Character> allCharacteres() {
			return characterRepository.findAll();
		}

		public Character findById(Long id) {
			Optional<Character> optionalShowId = characterRepository.findById(id);
			if(optionalShowId.isPresent()) {
				return optionalShowId.get();
			}
			return null;
		}
		
		
	//Update
		
		public Character updateCharacter(Character b) {
			return characterRepository.save(b);
		}
		
	//Delete
		
		public void deleteCharacter(Long id) {
			characterRepository.delete(findById(id));
		}
		
	//checks the number of teams in a Character
		
		public Character CharacterLimitChecker(Long CharacterId, BindingResult result) {
			List <Story> teams= findById(CharacterId).getStories();
			if (teams.size() < 5) {
				result.rejectValue("teams", "Matches", "Too many teams in this Character!");
	    		return null;
			}
			return null;
		}
}
