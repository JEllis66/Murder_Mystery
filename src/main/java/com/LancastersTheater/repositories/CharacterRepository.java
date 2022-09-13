package com.LancastersTheater.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.LancastersTheater.models.Character;

@Repository
public interface CharacterRepository extends CrudRepository<Character, Long> {

	List<Character> findAll();

	
	
}