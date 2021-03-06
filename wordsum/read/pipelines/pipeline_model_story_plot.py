# Open Story License
#
# Story: wordsum-python
# Writer: Kalab J. Oster(TM)
# Copyright Holders: Kalab J. Oster(TM)
# copyright (C) 2017 Kalab J. Oster(TM)
#
# Permission is granted by the Copyright Holders for humans or other intelligent agents to read, write, edit, publish and critique the Story
# if the humans or intelligent agents keep this Open Story License with the Story,
# and if the Story you tell remains free,
# and if another writer writes or edits the Story then the writer's name needs to be appended to the end of the Writer list of this Open Story License.


'''
Pipeline to plot story per chapter then as an entire book and use the distance of the vector change per chaper plot through
the story.

'''
import wordsum.read.utils.gensim2vec as gensim2vec
import wordsum.read.utils.etl4vec as etl4vec
import wordsum.read.utils.etl_wordsum as etl_wordsum
import logging
import json
import os
import wordsum.read.pipelines.utilities as utilities


PATH_SCRIPT=os.path.dirname(os.path.realpath(__file__))


def process(file, path_model_dump):
    logging.debug("pipeline_plot_story: Beginning.")

    file_list = utilities.get_file_list(file)

    # Make a book list for future use if required.
    book_list = []

    for f in file_list:
        logging.debug("pipeline_plot_story: Beginning logging.")
        # Open wordsum file.
        with open(f) as data_file:
            text_model = json.load(data_file)

        # Get only the narrator sentences and leave the dialog.
        narrative = etl_wordsum.get_text_model_narrator_paragraphs(text_model)

        # Replace punctuation, so we can group words.
        etl4vec.replace_punctuation_story(narrative)

        # Vector sentences of story now that we have removed punctuations.
        # This is done after the remove of punctuation like spaces with the em dash.
        etl4vec.list_sentences_in_story(narrative)

        # Reduce the lists of lists to a list of lists.
        story_list = etl4vec.list_story_lists(narrative)

        # D I A L O G
        # Get all the dialog.
        dialog = etl_wordsum.get_text_model_dialog_paragraphs(text_model)

        # Replace punctuation, so we can group words.
        etl4vec.replace_punctuation_story(dialog)

        # Vector sentences of story now that we have removed punctuations.
        # This is done after the remove of punctuation like spaces with the em dash.
        etl4vec.list_sentences_in_story(dialog)

        # Reduce the lists of lists to a list of lists.
        dialog_list = etl4vec.list_story_lists(dialog)

        # Print all the narrative to file.
        test_narrative = open(os.path.splitext(f)[0] + '.narrative', 'w')
        for items in story_list:
            line = ' '.join(items)
            test_narrative.write("%s\n" % line)

        # Print all the dialog (without carrying about character
        test_dialog = open(os.path.splitext(f)[0] + '.dialog', 'w')
        for items in dialog_list:
            line = ' '.join(items)
            test_dialog.write("%s\n" % line)

        # Get the origin file.
        file_basename = utilities.get_file_basename(f)

        # Create the model.
        model = gensim2vec.train_sentences(story_list)

        # Save the model to binary.
        gensim2vec.save_gensim2vec_model_binary(model, path_model_dump, file_basename)

        #  Save the text version.
        gensim2vec.save_gensim2vec_model_text(model, path_model_dump, file_basename)

        # If it is a directory and many files then assume chapters of sections and collect.
        if os.path.isdir(file):
            book_list.append(story_list)


    if os.path.isdir(file):

        logging.debug("pipeline_plot_story directory: " + file)
        book_list = etl4vec.list_story_lists(book_list)

        #print(os.path.basename(file))
        #print(book_list)

        # Create the model.
        model = gensim2vec.train_sentences(book_list)

        # Save the model to binary.
        gensim2vec.save_gensim2vec_model_binary(model, path_model_dump, os.path.basename(file))

        #  Save the text version.
        gensim2vec.save_gensim2vec_model_text(model, path_model_dump, os.path.basename(file))






